def factorial_recursive(num): # calculates the factorial of a number using recursion
    if num == 0 or num == 1: # base case: the factorial of 0 and 1 is 1
        return 1
    else:
        return num * factorial_recursive(num - 1) # recursive call to calculate the factorial of the number by multiplying it with the factorial of the number minus one

n = int(input("Enter a number to calculate its factorial: "))
if n < 0: # checks if the input number is negative, as factorial is not defined for negative numbers
    print("Factorial is not defined for negative numbers.")
else: # calculates and prints the factorial of the input number using the recursive function
    print(f"The factorial of {n} is: {factorial_recursive(n)}")