import matplotlib.pyplot as plt
from activations import ReLU
from layers import DenseLayer
from utils import spiral_data

X, y = spiral_data(100, 3)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
plt.show()

layer = DenseLayer(2, 5)
relu = ReLU()

layer.forward(X)
relu.forward(layer.output)
print(layer.output)
print(relu.output)
