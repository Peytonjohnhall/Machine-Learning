import pandas as pd

# define dataset
data = {
    "Comedy": [False, True, False, False, False, True, True, False, False, True, True, False],
    "Doctors": [True, False, False, False, False, False, False, True, True, True, True, False],
    "Lawyers": [False, True, True, True, False, False, False, True, True, False, False, False],
    "Guns": [False, False, True, False, True, True, False, True, False, False, True, False],
    "Likes": [False, True, True, False, False, True, True, True, False, True, False, False]
} # end bracket for data dictionary

df = pd.DataFrame(data)  # Create DataFrame

def predict_bayesian(df, new_data):
    """ Bayesian classifier prediction for the given attributes """

    # Calculation of prior probabilities
    p_likes = df["Likes"].mean()
    p_not_likes = 1 - p_likes
    
    # Calculation of conditional probabilities
    probabilities = {True: {}, False: {}}
    for feature in ["Comedy", "Doctors", "Lawyers", "Guns"]:
        probabilities[True][feature] = df[df["Likes"] == True][feature].mean()
        probabilities[False][feature] = df[df["Likes"] == False][feature].mean()
    
    # Calculation of likelihoods of the new data
    likelihood_true = p_likes
    likelihood_false = p_not_likes
    for feature, value in new_data.items():
        likelihood_true *= probabilities[True][feature] if value else (1 - probabilities[True][feature])
        likelihood_false *= probabilities[False][feature] if value else (1 - probabilities[False][feature])
    
    # Normalize the probabilities
    total = likelihood_true + likelihood_false
    prob_true = likelihood_true / total
    prob_false = likelihood_false / total
    
    return {"Likes": prob_true, "Does not like": prob_false}

def main():
    """ Main function to run Bayesian classifier on a new show """
    new_show = {"Comedy": True, "Doctors": True, "Lawyers": False, "Guns": False} # data to predict
    prediction = predict_bayesian(df, new_show)
    print("Prediction for new show:", prediction)

if __name__ == "__main__":
    main()