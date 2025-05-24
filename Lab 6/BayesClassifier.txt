from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def explanation_and_exploration():
	data = load_breast_cancer()

	print("Dataset Description:")
	print(data.DESCR)

	print("\nFeature Names:")
	print(data.feature_names)

	print("\nTarget Names:") # target classes
	print(data.target_names)

	print("\nDataset Shape:")
	print(data.data.shape)

	print("\nFirst 5 Samples:") # first 5 of the dataset
	print(data.data[:5])

	print("\nTargets for First 5 Samples:")
	print(data.target[:5])

def training_and_testing():
	data = load_breast_cancer()
	X, y = data.data, data.target

	# split data (i.e. 70% train, 30% test)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

	model = GaussianNB() # initialize GNB classifier

	model.fit(X_train, y_train) # train model

	y_pred = model.predict(X_test) # test model

	# calculate accuracy
	accuracy = accuracy_score(y_test, y_pred)
	print(f"Accuracy: {accuracy:.2f}")

def main():
	""" Give the user a choice """
	while True:
		try:
			choice = int(input("Type '1' + 'Enter/Return' to view an explanation of the dataset.\n"
								"Type '2' + 'Enter/Return' to view the accuracy of the algorithm.\n"
								"Type '3' + 'Enter/Return' to view both.\n"))
			if choice == 1:
				explanation_and_exploration()
			elif choice == 2:
				training_and_testing()
			elif choice == 3:
				explanation_and_exploration()
				training_and_testing()
			break # end loop
		except ValueError: # built-in exception
			print("Enter 1, 2, or 3.")

if __name__ == "__main__":
	main()