import pandas as pd
import numpy as np

def series_from_list():
    return pd.Series([7, 11, 13, 17])

def series_five_elements():
    return pd.Series([100.0] * 5)

def series_twenty_elements():
    series = pd.Series(np.random.randint(0, 101, size = 20))
    print("Descriptive Statistics:")
    print(series.describe())
    return series

def series_called_grades():
    return pd.Series([98.6, 77.9, 100, 83.4], index = ["Julie", "Charlie", "Sam", "Andera"])

def main():
    print("Series from list:")
    print(series_from_list())

    print("\nSeries with five elements:")
    print(series_five_elements())

    print("\nSeries with twenty elements:")
    series_twenty_elements()

    print("\nSeries called grades:")
    print(series_called_grades())

if __name__ == "__main__":
    main()