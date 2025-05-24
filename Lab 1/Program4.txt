""" 
A palindrome is a number, word or text phrase that reads the same backwards or
forwards. 
For example, each of the following five-digit integers is a palindrome: 
1234321, 5556555, 4505054, and 1176711. 
Write a script that reads in seven-digit integer and determines whether it’s a 
palindrome. 
"""

def is_palindrome(number):
    """ Compare strings to detect if a number is a palindrome """
    return str(number) == str(number)[::-1] # use slicing operation

def main():
    input_number = input("Enter a seven-digit integer: ")
    
    if input_number.isdigit() and len(input_number) == 7:
        try: # exception handling syntax
            number = int(input_number)
            if is_palindrome(number): # call the function
                print(f"{number} is a palindrome.")
            else:
                print(f"{number} is not a palindrome.")
        except ValueError: # catches a built-in exception
            print("There was an error processing your input.")
    else:
        print("Invalid input. Please ensure you enter a seven-digit integer.")

if __name__ == "__main__":
    main()
