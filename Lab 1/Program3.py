""" 
Implement a Fahrenheit function that returns the Fahrenheit equivalent of a 
Celsius temperature. Use the following formula:
F=(9/5)*C +32
Use this function to print a chart showing the Fahrenheit equivalents of all 
Celsius temperatures in the range 0–100 degrees. Use one digit of precision 
for the results. Print the outputs in a neat tabular format. 
"""

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

print("Celsius\tFahrenheit") # Column headers

# Create chart for Celsius temperatures from 0 to 100
for celsius in range(101):  # i.e. 0 to 100 inclusive
    fahrenheit = celsius_to_fahrenheit(celsius)
    # Print one decimal place for Fahrenheit
    print(f"{celsius}\t{fahrenheit:.1f}")
