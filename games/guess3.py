guess= None
value=10
live= 5

print("WELCOME TO OUR GAME")


while live > 0:
    print('Your life is {} '.format(live))
    
    guess = int(input("enter a number: "))
    
    if guess == value:
        print('you win')
        # print ("Do you want to play again?  ")
        another_attempt = input("Do you want to play again [ y| n ]?")
        if another_attempt == 'y':
             continue
        else:
            print('tnx for playing')
            break
    else:
        live -=1
else:
    print('game over')
