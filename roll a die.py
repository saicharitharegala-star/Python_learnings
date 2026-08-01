"""Write a program to stimulate the rolling of a die. A die has six phases with numbers from 1 to 6 printed on them
Each time the program is run, it should print a random number from 1 to 6. Use the random module to generate a random number."""
import random 
print("Welcome to the game of rolling of dice")
while True:
    choice = input("Press 'enter' to roll the die or 'q' to quit: ")
    choice = choice.strip().lower()
    if choice == 'q':
        print("Thanks for playing.byee!!")
        break
    elif choice == '':
        die_roll = random.randint(1,6)
        print(f" You rolled a {die_roll}")
    else : 
        print("Invalid input. please try again.")
print("Game over!!")