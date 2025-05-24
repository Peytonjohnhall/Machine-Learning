import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset globally so all functions can access it
wine = load_wine()
X = wine.data
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

def classes_features_dimensions_samples():
    print("Classes:", wine.target_names)
    print("Features:", wine.feature_names)
    print("Number of dimensions:", X.shape[1])
    print("Number of samples:", X.shape[0])

def bayesian_classifier():
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Bayesian Classifier Accuracy:", acc)
    return acc

def k_nearest_neighbor():
    best_acc = 0
    best_k = 0
    for k in [3, 5, 7, 9]:
        clf = KNeighborsClassifier(n_neighbors = k)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"KNN (k={k}) Accuracy:", acc)
        if acc > best_acc:
            best_acc = acc
            best_k = k
    return best_acc, best_k

def k_means_clustering():
    best_acc = 0
    best_k = 0
    for k in [3, 5, 7, 9]:
        kmeans = KMeans(n_clusters = k, random_state = 42, n_init = 10)
        kmeans.fit(X_train)
        y_pred_train = kmeans.predict(X_train)

        # Map each cluster to the most common true label in the train set
        labels = np.zeros(k)
        for i in range(k):
            mask = (y_pred_train == i)
            if np.sum(mask) == 0:
                labels[i] = -1 # fallback if cluster is empty
            else:
                labels[i] = mode(y_train[mask], keepdims = False)[0]

        # Predict test set and map to true labels
        y_pred_test = kmeans.predict(X_test)
        y_pred_mapped = np.array([labels[int(c)] for c in y_pred_test])

        acc = accuracy_score(y_test, y_pred_mapped)
        print(f"KMeans (k={k}) Accuracy (mapped):", acc)
        if acc > best_acc:
            best_acc = acc
            best_k = k
    return best_acc, best_k

def decision_tree():
    clf = DecisionTreeClassifier(random_state = 42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Decision Tree Accuracy:", acc)
    return acc

# Run all functions and collect results
classes_features_dimensions_samples()
bayes_acc = bayesian_classifier()
knn_acc, knn_k = k_nearest_neighbor()
kmeans_acc, kmeans_k = k_means_clustering()
tree_acc = decision_tree()

# Determine best algorithm
accuracies = {
    "Bayesian": bayes_acc,
    f"KNN (k={knn_k})": knn_acc,
    f"KMeans (k={kmeans_k})": kmeans_acc,
    "Decision Tree": tree_acc
}
best_algorithm = max(accuracies, key = accuracies.get)
print("Best Algorithm:", best_algorithm, "with accuracy:", accuracies[best_algorithm])