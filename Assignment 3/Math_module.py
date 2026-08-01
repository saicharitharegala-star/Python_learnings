import math #importing math module to use mathematical functions
num = float(input("Enter a number : "))

def calculate_square_root(num): # Define a function to calculate the square root of a number
    if num < 0:
        return "Square root is not defined for negative numbers."
    else:
        return math.sqrt(num)
print(f"The square root of {num} is {calculate_square_root(num)}")  

def calculate_logarithm(num): # Define a function to calculate the logarithm of a number
    if num <= 0:
        return "Logarithm is not defined for non-positive numbers."
    else:
        return math.log(num)
print(f"The logarithm of {num} is {calculate_logarithm(num)}")

def calculate_sine(num): # Define a function to calculate the sine of a number
    return math.sin(num)
print(f"The sine of {num} is {calculate_sine(num)}")