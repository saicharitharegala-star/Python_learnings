import math # imports the math module to perform mathematical operations
num = int(input("Enter a number : ")) # takes input from the user to perform mathematical operations using the math module

def calculate_square_root(num): # calculates the square root of a number using the math module
    if num<0:
        return "Square root is not defined for negative numbers."
    else:
        return math.sqrt(num)
print(f"The square root of {num} is: {calculate_square_root(num)}")

def calculate_logarithm(num): # calculates the logarithm of a number using the math module
    if num <= 0:
        return "Logarithm is not defined for non-positive numbers."
    else:
        return math.log(num)
print(f"The logarithm of {num} is : {calculate_logarithm(num)}")

def calculate_sine(num): # calculates the sine of a number using the math module
    return math.sin(num)
print(f"The sine of {num} is : {calculate_sine(num)}")