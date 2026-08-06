n = int(input("Enter a number : "))
def factorial(n):
    if n == 1 or n == 0:
        return 1 
    elif n<0 :
        return "Please enter a positive number"
    else :
        result = 1
        for i in range(1,n+1):
            result *= i
        return result

result = factorial(n)
    
print(f"The factorial of {n} is : {result}")


