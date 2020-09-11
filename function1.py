
def passwordProtector(password):
    answer = password
    user_submission = input("What's your password?")

    if user_submission == answer:
        print("You May Enter")
    else:
        print("You Can't Enter")

passwordProtector("Secret")