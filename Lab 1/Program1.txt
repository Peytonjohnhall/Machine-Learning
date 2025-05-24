"""
Write a script that calculates the squares and cubes of the numbers from 0 to 5. 
Print the resulting values in table format, as shown below. 
Use the tab escape sequence to achieve the three-column output.
"""

"""	\t = tab characters """
print("number\tsquare\tcube") # Column headers

for number in range(6): # i.e. 0 to 5
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")
