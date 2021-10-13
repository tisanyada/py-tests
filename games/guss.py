import random
attempts = 0
secretNumber = random.randint(1,100)
while True:
    print("Guess a number between 1 and 100. You can exit game anytime by typing q ")
    guess=input()
    stop=str(guess)
    if stop== 'q':
        print("You quitted the game")
        break
    elif not guess.isdigit():
        print("Only numbers are allowed")
    else:        
        guess = int(guess)
        attempts = attempts + 1
        if guess >100 or guess<=0:
            attempts = attempts - 1
            print("Not allowed.Only numbers between 1 and 100 allowed! \n")
        elif guess < secretNumber and guess >0:
            print("Nope!Try a higher number! \n")
        elif guess > secretNumber and guess <100:
            print("Nope!Try a lower number \n")
        if guess == secretNumber:
            attempts = str(attempts)
            print("Congratulations you found it after " + attempts + " attempts")
            break  