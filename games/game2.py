from random import randint
from time import sleep
chances = 4
elenco = []

random_number = randint(1, 25)
while chances > 0:
    num = input("Please Enter Number: ")
    if num == str(random_number):
        print("you win")
    else:
        elenco.append(num)
        print("\t These numbers are incorrect: " + "-".join(elenco))
        chances = chances - 1
        print("\tYou still have {} chances".format(chances) + "\n")

sleep(1)
print("\nGame over ")
print("The right answer was {}".format(random_number))