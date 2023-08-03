import numpy as np


class ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
