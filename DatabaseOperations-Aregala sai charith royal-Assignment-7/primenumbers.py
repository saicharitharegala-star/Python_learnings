number = int(input("Enter a number: "))


for i in range(2, number):
  if number % i == 0:
   print(number, "is not a prime number")
   break

print(number, "is a prime number")