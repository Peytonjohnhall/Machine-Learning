import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

digits = load_digits() # load digits dataset
X, y = digits.data, digits.target

# split dataset into 75% training and 25% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# create MLP model
mlp = MLPClassifier(hidden_layer_sizes = (64,), max_iter = 500, random_state = 1)

mlp.fit(X_train, y_train) # train model

y_pred = mlp.predict(X_test) # predict on test data

accuracy = accuracy_score(y_test, y_pred) # evaluate accuracy
print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# display a sample image with its prediction
plt.gray()
plt.matshow(digits.images[0]) # shows first image
plt.title(f"Label: {digits.target[0]}")
plt.show()