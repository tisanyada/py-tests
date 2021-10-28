Y="yes"
N="no"
PlayerOneScore=0
PlayerTwoScore=0

NoOfGamesInMatch=int(input("How many games? :- "))
while PlayerOneScore < NoOfGamesInMatch:
    PlayerOneWinsGame=str(input("Did Player 1 win the game?\n(Enter Y or N): "))

if PlayerOneWinsGame== "Y":
     PlayerOneScore= PlayerOneScore+1
else:
     PlayerTwoScore= PlayerTwoScore+1

print("Player 1: " ,PlayerOneScore)
print("Player 2: " ,PlayerTwoScore)

print("\n\nPress the RETURN key to end")