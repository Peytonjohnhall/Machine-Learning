import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = pd.read_csv("titanic-2.csv")

def correlation_class_survival():
    """ correlation_class_survival() analyzes and visualizes the c
        orrelation between passenger class and survival rate."""
    class_survival_rate = titanic_data.groupby("Pclass")["Survived"].mean()
    
    plt.figure(figsize = (8, 5))
    class_survival_rate.plot(kind = "bar", color = "skyblue")
    plt.title("Survival Rate by Passenger Class")
    plt.xlabel("Passenger Class")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation = 0)
    plt.show()

def gender_survival():
    """ gender_survival() investigates and visualizes 
        the impact of gender on the survival rate."""
    gender_survival_rate = titanic_data.groupby("Sex")["Survived"].mean()
    
    plt.figure(figsize = (8, 5))
    gender_survival_rate.plot(kind = "bar", color = "coral")
    plt.title("Survival Rate by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Rate")
    plt.xticks(rotation = 0)
    plt.show()

def family_quantity():
    """ family_quantity() determines the effect of the number of 
        siblings/spouses and parents/children on the survival rate."""
    # siblings/ spouses
    sibsp_survival_rate = titanic_data.groupby("SibSp")["Survived"].mean()
    # parents/ children
    parch_survival_rate = titanic_data.groupby("Parch")["Survived"].mean()
    
    plt.figure(figsize = (14, 6))
    plt.subplot(1, 2, 1)
    sibsp_survival_rate.plot(kind = "bar", color = "lightgreen")
    plt.title("Survival Rate by Number of Siblings/Spouses")
    plt.xlabel("Number of Siblings/Spouses")
    plt.ylabel("Survival Rate")
    
    plt.subplot(1, 2, 2)
    parch_survival_rate.plot(kind = "bar", color = "lightblue")
    plt.title("Survival Rate by Number of Parents/Children")
    plt.xlabel("Number of Parents/Children")
    plt.show()

def farepaid_survival():
    """ farepaid_survival() explores the 
        relationship between fare paid and survival."""
    plt.figure(figsize = (10, 6))
    sns.scatterplot(data = titanic_data, x = "Fare", y = "Survived", alpha = 0.6)
    plt.title("Relationship between Fare Paid and Survival")
    plt.xlabel("Fare")
    plt.ylabel("Survival Rate")
    plt.show()

correlation_class_survival()
gender_survival()
family_quantity()
farepaid_survival()