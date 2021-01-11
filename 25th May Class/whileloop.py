#To print the data 10 times:
i=0
while(i<10):
    print("Good Morning")
    i += 1

#while loop is used when we don't know how many times we want to repeat that loop:
#for loop is used when we know how many times we want to repeat the loop:
#check till the time user enter the corect number
guess = 25

while True:
    userguess = int(input("Enter the user guss value:"))
    if userguess==guess:
        print("Your guss value is correct..")
        break
    elif userguess>guess:
        print("Your value is more than guess value..")
    else:
        print("Your value is less than guess value...")

#Along with for and while loop we can take else block and else block executed when for or while loop terminated normally:
i=0
while i<10:
    print("Good Morning..",i)
    i += 3
else:
    print("else normal termination")

# 3 cases when else block will not be executed:
#   1. Abnormal termination or using break statement
#   2. when using exit function
#   3. when you get error message

#pass statement: when we have if condition but not have any body to write than we can keep pass in body and can't leave empty:
if i<10:
    pass #pass is empty statement in python cuz, we cannot leave empty
else:
    print("it's wrong")

while True:
    pass

def wish():
    pass

class MyClass:
    pass

#sum function use:
print(sum(range(1,11)))
print(sum(range(2,10,2))) #sum of range of 2,10 by stepping 2
