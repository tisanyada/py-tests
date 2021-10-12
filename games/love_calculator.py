print("Welcome to Love Calculator!")

name1 = input("What is your name? : ")
name2 = input("What is their name? : ")

combined = (name1 + name2).lower()
true_count = combined.count("t") + combined.count("r") + combined.count("u") + combined.count("e")
love_count = combined.count("l") + combined.count("o") + combined.count("v") + combined.count("e")
love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
