from sklearn.datasets import load_iris, load_digits
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def plot_elbow_method(data, dataset_name):
	k_range = range(1, 11)
	inertias = []

	for k in k_range:
		kmeans = KMeans(n_clusters = k, random_state = 42)
		kmeans.fit(data)
		inertias.append(kmeans.inertia_)

	plt.figure()
	plt.plot(k_range, inertias, marker = "o")
	plt.title(f"Elbow Method for {dataset_name}")
	plt.xlabel("Number of clusters (k)")
	plt.ylabel("Inertia")
	plt.grid(True)
	plt.show()

iris = load_iris()
iris_data = StandardScaler().fit_transform(iris.data)
plot_elbow_method(iris_data, "Iris")

digits = load_digits()
digits_data = StandardScaler().fit_transform(digits.data)
plot_elbow_method(digits_data, "MNIST Digits")