import random 
print("Welcome to the number guessing game!.You have a number to guess between 1 to 50 and you have 10 attempts!!")
secret_number = random.randint(1, 50)
attempts= 10
while attempts>0:
    guess = int(input("Enter your guess: "))
    print(f"Attempts left: {attempts}")
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        if guess < secret_number:
            print("Try higher!!")
        else:
            print("Try lower!!")

    attempts -= 1
if attempts == 0:
        print("Game over! You've used all your attempts. The secret number was:", secret_number)
