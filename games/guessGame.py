def main():
    print("this is the common sense game.")
    n = input("to begin please type 1: ")


    print("question 1: Do they have a fourth of July in England? ")
    q1 = str(input("enter yes or no: "))
    if q1 == "yes": 
        print(" no there is a fourth of July in America GAME OVER.")

    print("question 2: are there three outs in an inning of baseball?")
    q2 = str(input("enter yes or no: "))
    if q2 == "yes":
        print("no there are six GAME OVER")

    print("question 3: is it right to ignore a problem until it goes away? ")
    q3 = str(input("enter yes or no: "))
    if q3 == "no":
        print("solve the problem the moment it occurs don't wait GAME OVER")
    else:
        print("Common sense is instinct, but enough of it is Genius" "YOU WIN")
    main()
main()