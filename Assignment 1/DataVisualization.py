import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = pd.read_csv("titanic-2.csv")

def visualization():
    """ visualization() creates visualizations to show distribution of the variables: 
        age, passenger class, gender, and fare."""
    sns.set(style = "whitegrid")
    fig, axes = plt.subplots(2, 2, figsize = (14, 10))

    # histogram for age distribution
    sns.histplot(data = titanic_data, x = "Age", kde = True, ax = axes[0, 0])
    axes[0, 0].set_title("Distribution of Age")

    # count plot for passenger class
    sns.countplot(data = titanic_data, x = "Pclass", ax = axes[0, 1])
    axes[0, 1].set_title("Distribution of Passenger Class")

    # count plot for gender
    sns.countplot(data = titanic_data, x = "Sex", ax = axes[1, 0])
    axes[1, 0].set_title("Distribution of Gender")

    # histogram for fare distribution
    sns.histplot(data = titanic_data, x = "Fare", kde = True, ax = axes[1, 1])
    axes[1, 1].set_title("Distribution of Fare")

    plt.tight_layout()
    plt.show()

def pie_chart():
    """ pie_chart() generates a pie chart to illustrate the 
        age distribution of survivors to non-survivors."""
    age_by_survival = titanic_data.groupby("Survived")["Age"].mean()
    fig, ax = plt.subplots()
    ax.pie(age_by_survival, labels = ["Not Survived", "Survived"], autopct = "%1.1f%%", startangle = 90)
    ax.set_title("Average Age of Survivors vs Non-Survivors")
    plt.show()

def histogram():
    """ histogram() uses a histogram to visualize the age distribution of passengers."""
    plt.figure(figsize = (8, 6))
    sns.histplot(data = titanic_data, x = "Age", bins = 30, kde = True)
    plt.title("Age Distribution of Passengers")
    plt.show()

visualization()
pie_chart()
histogram()