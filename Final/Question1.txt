import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Basic preprocessing: drop columns and handle missing values
df = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Survived"]]
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Age"].fillna(df["Age"].median(), inplace = True)

# Define features and target
X = df.drop("Survived", axis = 1)
y = df["Survived"]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# 1. Decision Tree Classifier
tree_clf = DecisionTreeClassifier(random_state = 42)
tree_clf.fit(X_train, y_train)
y_pred_tree = tree_clf.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_tree))

# 2. Plot the Decision Tree
plt.figure(figsize = (20,10))
plot_tree(tree_clf, feature_names = X.columns, class_names = ["Died", "Survived"], filled = True)
plt.show()

# 3. KNN Classifier with different k values
for k in [3, 5, 7, 9]:
    knn_clf = KNeighborsClassifier(n_neighbors = k)
    knn_clf.fit(X_train, y_train)
    y_pred_knn = knn_clf.predict(X_test)
    print(f"KNN (k={k}) Accuracy:", accuracy_score(y_test, y_pred_knn))