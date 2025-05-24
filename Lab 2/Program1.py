"""
(10 points) Program 1: Summarizing Letters in String
Write a function summarize_letters that receives a string and returns a list 
of tuples containing the unique letters and their frequencies in the string. 
Test your function and display each letter with its frequency. Your function 
should ignore case sensitivity (that is, ‘a’ and ‘A’ are the same) and ignore 
spaces. When done, write a statement that says whether the string has all the 
letters of the alphabet or not.
"""

from collections import Counter
import string

def summarize_letters(input_string):
    # use lower() function and remove spaces to normalize the string
    normalized_string = ''.join(filter(str.isalpha, input_string.lower()))
    
    # count frequencies of each letter
    letter_counts = Counter(normalized_string)
    
    # convert counter to a list of tuples and sort by letter
    summary = sorted(letter_counts.items())
    
    # check if all letters of the alphabet are present
    alphabet_set = set(string.ascii_lowercase)
    string_letters_set = set(normalized_string)
    has_all_letters = alphabet_set <= string_letters_set
    
    for letter, count in summary:
        print(f"{letter}: {count}") # print each letter with its frequency
    
    if has_all_letters: # call the variable
        print("The string has all the letters of the alphabet.")
    else:
        print("The string does not have all the letters of the alphabet.")
    
    return summary

if __name__ == "__main__":
    user_input = input("Enter a string to analyze: ")
    summarize_letters(user_input)