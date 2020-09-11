def yearlywage():
    hourlywage = int(input("How much money do you make per hour?"))
    hoursperweek = int(input("How many hours do you work per week?"))
    weeklyincome = hourlywage * hoursperweek
    return weeklyincome * 52

usersincome = yearlywage()
print("Your are currently making $", usersincome, "Per Year!")
  