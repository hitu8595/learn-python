userLives = int(input("How many lves do  currrently have? "))

if userLives >= 3:
    print("You have enough lives.. please don't worry")
elif userLives == 2:
    print("You should proceed with caution")
elif userLives == 1:
    print("You're almost dead")
else:
    print("Game Over")