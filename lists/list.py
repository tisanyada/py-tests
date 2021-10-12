guess = None 
value = 5
print("welcome to our guess game")
while guess != value:
    guess = int(input("enter a number:"))
    if guess == value:
        print("you win")

while guess != value:
    guess = int(input("enter a number:"))
    if guess == "1,2,3,4":
        print("lose life")