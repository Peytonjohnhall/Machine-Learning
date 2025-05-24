import matplotlib.pyplot as plt
import math

def read_data(file_path):
	""" read data from txt file """
	data = []
	with open(file_path, "r") as file:
		for line in file:
			x, y, label = map(int, line.strip().split("\t"))
			data.append((x, y, label))
	return data

def euclidean_distance(p1, p2):
	""" compute euclidean distance between two points """
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def classify_point(training_data, test_point, k):
	""" classify a point based on knn """
	distances = []

	# find distance between test and training point
	for train_point in training_data:
		d = euclidean_distance(train_point, test_point)
		distances.append((d, train_point[2])) # store distance and label

	distances.sort() # ascending order

	k_nearest = distances[:k] # select the k nearest neighbors

	# count votes per class label
	class_votes = {}
	for _, label in k_nearest: # among the k neighbors
		if label not in class_votes:
			class_votes[label] = 0
		class_votes[label] += 1

	return max(class_votes, key = class_votes.get)

def visualize_data(training_data, test_data, predicted_labels):
	""" visualize the dataset """

	# define colors and shapes for the three classes
	colors = {1: "red", 2: "blue", 3: "green"}
	shapes = {1: "o", 2: "s", 3: "D"}

	# plot training points using color and shape
	for x, y, label in training_data:
		plt.scatter(x, y, color = colors[label], marker = shapes[label], 
						  label = f"class {label}" if f"class {label}" not in 
						  plt.gca().get_legend_handles_labels()[1] else "")

	# plot test points using predicted color and black-edged "x" marker
	for i, (x, y, _) in enumerate(test_data):
		pred_label = predicted_labels[i]
		plt.scatter(x, y, color = colors[pred_label], marker = "X", 
						  edgecolors = "black", s = 100)

	plt.title("knn classification results")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid(True)
	plt.legend()
	plt.show()

if __name__ == "__main__":
	training_file = "points_training.txt"
	test_file = "points_test.txt"
	k = 5 # chosen for a balance between bias and variance

	training_data = read_data(training_file)
	test_data = read_data(test_file)

	predicted_labels = []
	for point in test_data:
		label = classify_point(training_data, point, k)
		predicted_labels.append(label)

	visualize_data(training_data, test_data, predicted_labels)