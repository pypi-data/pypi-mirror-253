"""
DeepSpeech2 model
"""

import math

import mindspore.nn as nn
import mindspore.ops as ops
import numpy as np
from mindspore import Tensor


class SequenceWise(nn.Cell):
    """
    SequenceWise FC Layers.
    """

    def __init__(self, module):
        super(SequenceWise, self).__init__()
        self.module = module
        self.reshape_op = ops.Reshape()
        self.shape_op = ops.Shape()
        self._initialize_weights()

    def construct(self, x):
        sizes = self.shape_op(x)
        t, n = sizes[0], sizes[1]
        x = self.reshape_op(x, (t * n, -1))
        x = self.module(x)
        x = self.reshape_op(x, (t, n, -1))
        return x

    def _initialize_weights(self):
        self.init_parameters_data()
        for _, m in self.cells_and_names():
            if isinstance(m, nn.Dense):
                m.weight.set_data(
                    Tensor(
                        np.random.uniform(
                            -1.0 / m.in_channels,
                            1.0 / m.in_channels,
                            m.weight.data.shape,
                        ).astype("float32")
                    )
                )
                if m.bias is not None:
                    m.bias.set_data(
                        Tensor(
                            np.random.uniform(
                                -1.0 / m.in_channels,
                                1.0 / m.in_channels,
                                m.bias.data.shape,
                            ).astype("float32")
                        )
                    )


class MaskConv(nn.Cell):
    """
    MaskConv architecture.
    """

    def __init__(self):
        super(MaskConv, self).__init__()
        self.zeros = ops.ZerosLike()
        self.conv1 = nn.Conv2d(
            1,
            32,
            kernel_size=(41, 11),
            stride=(2, 2),
            pad_mode="pad",
            padding=(20, 20, 5, 5),
        )
        self.bn1 = nn.BatchNorm2d(num_features=32)
        self.conv2 = nn.Conv2d(
            32,
            32,
            kernel_size=(21, 11),
            stride=(2, 1),
            pad_mode="pad",
            padding=(10, 10, 5, 5),
        )
        self.bn2 = nn.BatchNorm2d(num_features=32)
        self.tanh = nn.Tanh()
        self._initialize_weights()
        self.module_list = nn.CellList(
            [self.conv1, self.bn1, self.tanh, self.conv2, self.bn2, self.tanh]
        )

    def construct(self, x, lengths):
        for module in self.module_list:
            x = module(x)
        return x

    def _initialize_weights(self):
        """
        parameter initialization
        """
        self.init_parameters_data()
        for _, m in self.cells_and_names():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.set_data(
                    Tensor(
                        np.random.normal(
                            0, np.sqrt(2.0 / n), m.weight.data.shape
                        ).astype("float32")
                    )
                )
                if m.bias is not None:
                    m.bias.set_data(
                        Tensor(np.zeros(m.bias.data.shape, dtype="float32"))
                    )
            elif isinstance(m, nn.BatchNorm2d):
                m.gamma.set_data(Tensor(np.ones(m.gamma.data.shape, dtype="float32")))
                m.beta.set_data(Tensor(np.zeros(m.beta.data.shape, dtype="float32")))


class BatchRNN(nn.Cell):
    """
    BatchRNN architecture.
    Args:
        batch_size(int):  smaple_number of per step in training
        input_size (int):  dimension of input tensor
        hidden_size(int):  rnn hidden size
        num_layers(int):  rnn layers
        bidirectional(bool): use bidirectional rnn (default=True). Currently, only bidirectional rnn is implemented.
        batch_norm(bool): whether to use batchnorm in RNN.
        rnn_type (str):  rnn type to use (default='LSTM'). Currently, only LSTM is supported.
    """

    def __init__(
        self,
        batch_size,
        input_size,
        hidden_size,
        num_layers,
        bidirectional=False,
        batch_norm=False,
        rnn_type="LSTM",
    ):
        super(BatchRNN, self).__init__()
        self.batch_size = batch_size
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn_type = rnn_type
        self.bidirectional = bidirectional
        self.has_bias = True
        self.is_batch_norm = batch_norm
        self.num_directions = 2 if bidirectional else 1
        self.reshape_op = ops.Reshape()
        self.shape_op = ops.Shape()
        self.sum_op = ops.ReduceSum()

        input_size_list = [input_size]
        for i in range(num_layers - 1):
            input_size_list.append(hidden_size)
        layers = []

        for i in range(num_layers):
            layers.append(
                nn.LSTM(
                    input_size=input_size_list[i],
                    hidden_size=hidden_size,
                    bidirectional=bidirectional,
                    has_bias=self.has_bias,
                )
            )
        self.lstms = nn.CellList(layers)

        if batch_norm:
            batch_norm_layer = []
            for i in range(num_layers - 1):
                batch_norm_layer.append(nn.BatchNorm1d(hidden_size))
            self.batch_norm_list = batch_norm_layer

    def construct(self, x):
        for i in range(self.num_layers):
            if self.is_batch_norm and i > 0:
                x = self.batch_norm_list[i - 1](x)
            x, _ = self.lstms[i](x)
            if self.bidirectional:
                size = self.shape_op(x)
                x = self.reshape_op(x, (size[0], size[1], 2, -1))
                x = self.sum_op(x, 2)
        return x


class DeepSpeechModel(nn.Cell):
    """
    DeepSpeechModel.
    Args:
        batch_size(int):  smaple_number of per step in training (default=128)
        rnn_type (str):  rnn type to use (default="LSTM")
        labels (list):  list containing all the possible characters to map to
        rnn_hidden_size(int):  rnn hidden size
        nb_layers(int):  number of rnn layers
        audio_conf: Config containing the sample rate, window and the window length/stride in seconds
        bidirectional(bool): use bidirectional rnn (default=True)
    """

    def __init__(
        self,
        batch_size,
        labels,
        rnn_hidden_size,
        nb_layers,
        audio_conf,
        rnn_type="LSTM",
        bidirectional=True,
    ):
        super(DeepSpeechModel, self).__init__()
        self.batch_size = batch_size
        self.hidden_size = rnn_hidden_size
        self.hidden_layers = nb_layers
        self.rnn_type = rnn_type
        self.audio_conf = audio_conf
        self.labels = labels
        self.bidirectional = bidirectional
        self.reshape_op = ops.Reshape()
        self.shape_op = ops.Shape()
        self.transpose_op = ops.Transpose()
        self.add = ops.Add()
        self.div = ops.Div()

        sample_rate = self.audio_conf.sample_rate
        window_size = self.audio_conf.window_size
        num_classes = len(self.labels)

        self.conv = MaskConv()
        # This is to calculate
        self.pre, self.stride = self.get_conv_num()

        # Based on above convolutions and spectrogram size using conv formula (W - F + 2P)/ S+1
        rnn_input_size = int(math.floor((sample_rate * window_size) / 2) + 1)
        rnn_input_size = int(math.floor(rnn_input_size + 2 * 20 - 41) / 2 + 1)
        rnn_input_size = int(math.floor(rnn_input_size + 2 * 10 - 21) / 2 + 1)
        rnn_input_size *= 32

        self.RNN = BatchRNN(
            batch_size=self.batch_size,
            input_size=rnn_input_size,
            num_layers=nb_layers,
            hidden_size=rnn_hidden_size,
            bidirectional=bidirectional,
            batch_norm=False,
            rnn_type=self.rnn_type,
        )
        fully_connected = nn.Dense(rnn_hidden_size, num_classes, has_bias=False)
        self.fc = SequenceWise(fully_connected)

    def construct(self, x, lengths):
        """
        lengths is actually not used in this part since Mindspore does not support dynamic shape.
        """
        output_lengths = self.get_seq_lens(lengths)
        x = self.conv(x, lengths)
        sizes = self.shape_op(x)
        x = self.reshape_op(x, (sizes[0], sizes[1] * sizes[2], sizes[3]))
        x = self.transpose_op(x, (2, 0, 1))
        x = self.RNN(x)
        x = self.fc(x)
        return x, output_lengths

    def get_seq_lens(self, seq_len):
        """
        Given a 1D Tensor or Variable containing integer sequence lengths, return a 1D tensor or variable
        containing the size sequences that will be output by the network.
        """
        for i in range(len(self.stride)):
            seq_len = self.add(
                self.div(self.add(seq_len, self.pre[i]), self.stride[i]), 1
            )
        return seq_len

    def get_conv_num(self):
        p, s = [], []
        for _, cell in self.conv.cells_and_names():
            if isinstance(cell, nn.Conv2d):
                kernel_size = cell.kernel_size
                padding_1 = int((kernel_size[1] - 1) / 2)
                temp = 2 * padding_1 - cell.dilation[1] * (cell.kernel_size[1] - 1) - 1
                p.append(temp)
                s.append(cell.stride[1])
        return p, s
