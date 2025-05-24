import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

data = [
    ["slashdot", "USA", "yes", 18, "None"],
    ["google", "France", "yes", 23, "Premium"],
    ["digg", "USA", "yes", 24, "Basic"],
    ["kiwitobes", "France", "yes", 23, "Basic"],
    ["google", "UK", "no", 21, "Premium"],
    ["(direct)", "New Zealand", "no", 12, "None"],
    ["(direct)", "UK", "no", 21, "Basic"],
    ["google", "USA", "no", 24, "Premium"],
    ["slashdot", "France", "yes", 19, "None"],
    ["digg", "USA", "no", 18, "None"],
    ["google", "UK", "no", 18, "None"],
    ["kiwitobes", "UK", "no", 19, "None"],
    ["digg", "New Zealand", "yes", 12, "Basic"],
    ["google", "UK", "yes", 18, "Basic"],
    ["kiwitobes", "France", "yes", 19, "Basic"]
]

df = pd.DataFrame(data, columns = ["Referrer", "Location", "Read FAQ", 
                                   "Pages Viewed", "Service Chosen"])

# label encode categorical columns
le_referrer = LabelEncoder()
le_location = LabelEncoder()
le_read = LabelEncoder()
le_service = LabelEncoder()

df["Referrer"] = le_referrer.fit_transform(df["Referrer"])
df["Location"] = le_location.fit_transform(df["Location"])
df["Read FAQ"] = le_read.fit_transform(df["Read FAQ"])
df["Service Chosen"] = le_service.fit_transform(df["Service Chosen"])

# split data
X = df[["Referrer", "Location", "Read FAQ", "Pages Viewed"]]
y = df["Service Chosen"]

# train model
clf = DecisionTreeClassifier(random_state = 42)
clf.fit(X, y)

# predict
input_data = pd.DataFrame([[
    le_referrer.transform(["(direct)"])[0],
    le_location.transform(["USA"])[0], # location = USA
    le_read.transform(["yes"])[0], # read FAQ = yes
    5
]], columns = ["Referrer", "Location", "Read FAQ", "Pages Viewed"])

prediction = clf.predict(input_data)
print("Predicted service:", le_service.inverse_transform(prediction)[0])

# plot tree
plt.figure(figsize=(16, 8))
plot_tree(clf, feature_names = ["Referrer", "Location", "Read FAQ", 
                                "Pages Viewed"],
          class_names = le_service.classes_,
          filled = True)
plt.title("Decision Tree for Service Choice")
plt.show()