
import random
def main():

    roll = random.randint(1, 6)
    print(roll)
#taking user input
    user_guess = input("Guess a number between 1 and 6: ")
    if user_guess == roll:
        print("You guessed correctly!")
    else:
        print("Better luck next time.")
    
main()
    