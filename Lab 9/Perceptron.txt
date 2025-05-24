import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

class Perceptron:
	def __init__(self, lr=0.01, n_epochs=100):
		self.lr = lr
		self.n_epochs = n_epochs
		self.weights = None
		self.bias = None

	def fit(self, X, y):
		n_samples, n_features = X.shape
		self.weights = np.zeros(n_features)
		self.bias = 0

		for _ in range(self.n_epochs):
			for idx, x_i in enumerate(X):
				linear_output = np.dot(x_i, self.weights) + self.bias
				y_predicted = np.where(linear_output >= 0, 1, 0)
				update = self.lr * (y[idx] - y_predicted)
				self.weights += update * x_i
				self.bias += update

	def predict(self, X):
		linear_output = np.dot(X, self.weights) + self.bias
		return np.where(linear_output >= 0, 1, 0)

# generate linearly separable data
X, y = make_classification(n_samples = 100, n_features = 2, n_redundant = 0,
                           n_informative = 2, n_clusters_per_class = 1, n_classes = 2)

# train the perceptron
perceptron = Perceptron(lr = 0.01, n_epochs = 100)
perceptron.fit(X, y)

# plot the decision boundary
def plot_decision_boundary(X, y, model):
	x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
	y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
	grid = np.c_[xx.ravel(), yy.ravel()]
	preds = model.predict(grid).reshape(xx.shape)

	plt.contourf(xx, yy, preds, alpha = 0.3, cmap = plt.cm.Paired)
	plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.Paired, edgecolors = "k")
	plt.title("Perceptron Decision Boundary")
	plt.xlabel("Feature 1")
	plt.ylabel("Feature 2")
	plt.show()

plot_decision_boundary(X, y, perceptron)

# accuracy report
predictions = perceptron.predict(X)
accuracy = np.mean(predictions == y)
print(f"Training Accuracy: {accuracy * 100:.2f}%")
