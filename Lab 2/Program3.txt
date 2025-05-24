"""
(10 points) Program 3: Numbers Frequency
Write a program that generates 100 random numbers between 1 and 10. The program 
should store the frequency of each number generated in a dictionary with the 
number as the key and the amount of times it has occurred as the value. For 
example, if the program generates the number 6 a total of 11 times, the 
dictionary will contain a key of 6 with an associated value of 11. Once all of 
the numbers have been generated, display information about the frequency of 
each number.
"""

import random

def generate_numbers_frequency():
    frequency_dict = {} # dictionary stores the frequency of each number

    # generate 100 random numbers between 1 and 10
    for i in range(100):
        number = random.randint(1, 10)
        if number in frequency_dict:
            frequency_dict[number] += 1 # equals itself plus 1
        else:
            frequency_dict[number] = 1

    # print the frequency of each number
    for number in range(1, 11):
        print(f"Number {number}: {frequency_dict.get(number, 0)} times")

if __name__ == "__main__":
    generate_numbers_frequency()