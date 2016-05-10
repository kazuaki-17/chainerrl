import chainer
from chainer import links as L

import crelu


class NatureDQNHeadCReLU(chainer.ChainList):

    def __init__(self, n_input_channels=4, n_output_channels=512):
        self.n_input_channels = n_input_channels
        self.n_output_channels = n_output_channels

        layers = [
            L.Convolution2D(n_input_channels, 32 // 2, 8, stride=4),
            L.Convolution2D(32, 64 // 2, 4, stride=2),
            L.Convolution2D(64, 64 // 2, 3, stride=1),
            L.Linear(3136, n_output_channels // 2),
        ]

        super(NatureDQNHeadCReLU, self).__init__(*layers)

    def __call__(self, state):
        h = state
        for layer in self:
            h = crelu.crelu(layer(h))
        return h


class NIPSDQNHeadCReLU(chainer.ChainList):

    def __init__(self, n_input_channels=4, n_output_channels=256):
        self.n_input_channels = n_input_channels
        self.n_output_channels = n_output_channels

        layers = [
            L.Convolution2D(n_input_channels, 16 // 2, 8, stride=4),
            L.Convolution2D(16, 32 // 2, 4, stride=2),
            L.Linear(2592, n_output_channels // 2),
        ]

        super(NIPSDQNHeadCReLU, self).__init__(*layers)

    def __call__(self, state):
        h = state
        for layer in self:
            h = crelu.crelu(layer(h))
        return h