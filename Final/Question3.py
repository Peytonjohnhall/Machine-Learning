import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Create parity dataset (3 inputs)
X = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])
# Label 1 if number of ones is even, else 0
y = np.array([1,0,0,1,0,1,1,0])

# 1. Can Perceptron learn this?
perceptron = Perceptron(max_iter = 1000, tol = 1e-3, random_state = 42)
perceptron.fit(X, y)
y_pred_perceptron = perceptron.predict(X)
acc_perceptron = accuracy_score(y, y_pred_perceptron)
print("Perceptron Accuracy:", acc_perceptron)

# 2. Show how Perceptron learns
print("Perceptron predictions:", y_pred_perceptron)

# 3. Show how Multi-layer Perceptron learns
mlp = MLPClassifier(hidden_layer_sizes = (5,), max_iter = 1000, random_state = 42)
mlp.fit(X, y)
y_pred_mlp = mlp.predict(X)
acc_mlp = accuracy_score(y, y_pred_mlp)
print("MLP Accuracy:", acc_mlp)
print("MLP predictions:", y_pred_mlp)