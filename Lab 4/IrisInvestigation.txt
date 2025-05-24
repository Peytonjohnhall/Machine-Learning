"""
(25 points) Program 1: Working with IRIS dataset using
Pandas
Iris dataset is a popular dataset for machine learning, which contains 150 
records of information about three Iris plant species. The Iris dataset is 
available from various online sources, including Kaggle
https://www.kaggle.com/uciml/iris/home . Investigate the Iris dataset’s 
columns, then perform the following tasks to study and analyze the dataset:
1. Download Iris.csv from one of the dataset repositories.
2. Load the dataset into a pandas DataFrame with the following statement, which 
uses the first column of each record as the row index:
df = pd.read_csv('Iris.csv', index_col=0)
3. Display the DataFrame’s head.
4. Display the DataFrame’s tail.
5. Use the DataFrame method describe to calculate the descriptive statistics 
for the numerical data columns—Sepal Length Cm, Sepal Width Cm, Petal Length Cm 
and Petal Width Cm.
6. Use matplotlib to view histograms of each numerical data colu
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv', index_col=0) # load dataset

print("Head of the DataFrame:")
print(df.head()) # first few rows of the DataFrame

print("\nTail of the DataFrame:")
print(df.tail()) # last few rows of the DataFrame

print("\nDescriptive Statistics:")
print(df.describe()) # for the numerical data columns

plt.figure(figsize=(10, 8))
for i, column in enumerate(df.columns[:-1], 1): # exclude last column
    plt.subplot(2, 2, i) # create subplot in grid
    df[column].hist(bins=20) # plot histogram for column data
    plt.title(column) # call loop variable

plt.tight_layout()
plt.show()