""" Use if statements to determine whether an input integer is odd or even. """

number = int(input("Enter an integer: "))

if number % 2 == 0: # any even int mod 2 always = 0
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")
