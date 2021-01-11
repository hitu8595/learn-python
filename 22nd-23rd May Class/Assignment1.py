#checking the year is leap year or not
number = int(input("Please enter the number: "))

if number%4 == 0:
    print(number, "is a leap year")
else:
    print(number, "is not a leap year")

#check number is even or odd
num = int(input("Please enter any number: "))

if num%2 == 0:
    print(num, "is a even number")
else:
    print(num, "is a odd number")

#take 2 numbers from end user and print the bigger number
a = int(input("Please Enter First Number: "))
b = int(input("Please Enter Second Number: "))

if a>=b:
    print(a, "is the biggest number")
else:
    print(b, "is the biggest number")

# Take 2 numbers from user and chek positive/negative and print even and odd after that
num1 = int(input("Please Enter First Number: "))
 
if num1>=0 and num1%2 == 0:
    print(num1, "is positive and even number")
elif num1>=0 and num1%2 != 0:
    print(num1, "is positive and odd number")
elif num1<0 and num1%2==0:
    print(num1, "is negative and even number")
else:
    print(num1, "is negative and odd number")

#Login with username and password:
username = input("Enter username: ")
password = input("Enter password: ")
if  username=='Hitu' and password=='Patel':
    print("Login Successful")
else:
    print("Login Fail")

#Take the number rom end suer and check positive negative or zero:
number = int(input("Enter the number: "))
if number>0:
    print(f"{number} is positive")
elif number<0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
 
#Take the day from end user and print discount according to day else print error date:
day = input("Enter the day: ")
if day=="mon" or day=="tue":
    print(f"You've recived 2% discount")
elif day=="wed" or day=="thurs" or day=="fri":
    print(f"You've recived 3% discount")
elif day=="sat" or day=="sun":
    print(f"You've recived 5% discount")
else:
    print(f"Please enter proper information")

#Take the name and marks from the end user and give the grade accordingly
name = input("Enter your name: ")
english_marks = int(input("Enter your english obtained marks: "))
science_marks = int(input("Enter your science obtained marks: "))
maths_marks = int(input("Enter your maths obtained marks: "))

total_marks = english_marks+science_marks+maths_marks
percentage = (total_marks/300)*100
grade = 'x'

if percentage>70:
    grade = "A"
elif percentage>60 and percentage<69:
    grade = "B"
elif percentage>50 and percentage<59:
    grade = "C"
elif percentage>40 and percentage<49:
    grade = "D"
else:
    print("Sorry, you're fail")
print(f"Hi {name} your total mark is {total_marks} and grade is {grade}")

#Take the pin 1234 and also take another pin from end user match it till 4 attempts and if not print byebye
pin = 1234
for x in range(1,5):
    user_pin = int(input("Enter valid pin: "))
    if pin == user_pin:
            print("Congratulations")
            break
    if x==4:
        print("Bye Bye... your attemption period is done")

#Take name from the user and cehck vovels and consonants
name = input("Enter the name: ")
vovels = ""
consonants = ""
for x in name:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        vovels += x
    else:
        consonants += x
print(f"Vovels are {vovels}")
print(f"Consonants are {consonants}")

#Take the name from the user and print the addition of code values:
name = input("Enter the name: ")
sum = 0
for x in name:
    sum += ord(x)
print("Result...",sum)
