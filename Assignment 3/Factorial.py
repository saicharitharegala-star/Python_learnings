def factorial_recursive(n): # Define a recursive function to calculate factorial
    if n < 0:   # Handle the case for negative numbers
        return "Factorial is not defined for negative numbers."

    elif n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
     result = n * factorial_recursive(n-1) # Recursive call to calculate factorial of n-1
    return result 
n = float(input("Enter a non-negative integer to calculate it's factorial: "))
print(f"The factorial of {n} is {factorial_recursive(n)}")