import pandas as pd

titanic_data = pd.read_csv("titanic-2.csv")

print(titanic_data.head()) # display first few rows

print(titanic_data.describe(include = "all")) # display summary statistics

print(titanic_data.isnull().sum()) # identify missing values

# fill missing numerical values with the mean
titanic_data.fillna(titanic_data.mean(), inplace = True)
print(titanic_data.isnull().sum()) # check for missing values