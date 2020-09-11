password = "nothing"
tries = 0

while password != "secret":
    tries = tries + 1
    password = input("what is the secret password?")
    print("sorry please try agaian")
    if tries == 3:
        print("You have been locked out")
        exit()

print("Correct! Yoy may Enter")