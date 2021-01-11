#Flow control statement
# 1. Conditional statement --> if, if-else, elif
# 2. Looping/Iteration statement --> for, while
# 3. Transfer statements --> break, continue, return, try

# 1. Conditional statements(IF): ONLY IF CONDITION.. CONDITION IS TRUE ANSWER WILL PRINT OTHERWISE CODE WILL NOT GET EXECUTED
x,y = 60,20
if(x>y):
    print("Answer is right")

# 1. Conditional statement(if-else): true or false answer will come
if 10>20:
    print("Answer is wrong")
else:
    print("You're right")

# example2:
if True:
    print("Answer is wrong")
else:
    print("You're right")

# example3: other than true and false it'll give true answer
if "Hitu":
    print("Answer is wrong")
else:
    print("You're right")

#example4: 0 can bebconsider as false
if 0:
    print("Answer is wrong")
else:
    print("You're right")

#example5: other way of writing if-else.. if condition is true answer will be"Hi Hitu" else answer will be "Hi Mumma"
print("Hi Hitu") if 5>2 else print("Hi Mumma")
# Multiple statement -print but not recomended go with alignment
{print("Hi Hitu"), print("Hi Dad")} if 5>2 else {print("Hi Mumma"), print("Hi Bro")}

#Example5:
x = 200 if 10<20 else 100
print(x)

# 1. elif -- takes more than 2 option and must end with else block
#ex1:
a = 10
if a==10:
    print("GM")
elif a==20:
    print("GA")
elif a==30:
    print("GE")
else:
    print("GN")