userNumber = int(input("What is your favorite number"))

if userNumber > 0 and userNumber < 10:
    print("You choose wrong number")
elif userNumber >= 10:
    print("You are jackpot winner")
elif userNumber < 0:
    print("You are loser")
else:
    print("You are out of game")

