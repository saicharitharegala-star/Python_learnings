n = int(input("Enter a number:"))
def recursive_function(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        return n*recursive_function(n-1)

result = recursive_function(n)
print("The factorial of", n, "is", result)
    
