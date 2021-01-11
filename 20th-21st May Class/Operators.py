#Arithmatic Operator
x,y = 15,4
print(x+y)
print(x-y)
print(x*y)
#division returns float values
print(x/y)
#will return remainder
print(x%y)
#floor division returns int values
print(x//y)
#Power value
print(x**y)

#Operator Precedence:
#() 
# *, /, %
# +, -
print(10/2 - 3%2 + (3+2) *5)

#Rational Operators,:: It returns boolean value
a,b = 5,2
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#Bitwise Operator : & | not(returns boolean value)
#Truth table
# A     B   A&B  A|B
# t/1  t/1   t    t
# t/1  f/0   f    t
# f/0  t/1   f    t
# f/0  f/0   f    f

# Data represetation: 32  16  8  4  2  1
#  8 and 2 clocks are enabled 1  0  1  0 = 10 (8+2)
#                             0  1  0  1 = 5
#                             1  1  1  0 = 14
#                     1   0   0  0  1  1 = 35
# For below 10 & 8 ... write data representation for 10 and 8... 1 0 1 0 (10) & 1 0 0 0(8)
#Perform AND operator after that
print(10&8)

# Python will convert any method into code language and after it'll conver into byte code (8 4 2 1) by machine
# and will give you output
#To see the code value in otyhon we use "ord" function
print(ord('a'))
print(ord('b'))
print(ord('A'))

#To see the character value from code use "chr" function
print(chr(97))
print(chr(50))
print(chr(52))

# not - other than true or false it returns true
print(not False)
print(not True) 
print(not 0)
print(not 1)
print(not 23)
print(not "Hitu")

#Logical Operators: for other lang (& && can be find but in python it's like & and)
#cond1 & Cond2 - it'll check both the conditions then only it'll give result
#cond1 and cond2: Here, the second condition execution depends on first condition
#if the first condition is true than only second condition will exec
#if the first condition is false then second condition will not exec
#Below & example will get type error cuz, string and int are 2 different data types
if(10>20) & (10+"Hitu"=="10Hitu"):
    print("Answer is right")
else:
    print("Answer is wrong")

#and condition example.. op will be "Answer is wrong"
if(10>20) and (10+"Hitu"=="10Hitu"):
    print("Answer is right")
else:
    print("Answer is wrong")

#FOr, & operation paranthases requires but for "and" paranthases are not required (cuz, and is keyword)
# cond1 | cond2 : it'll execute both codition..if anyof the condition is true will return true
# cond1 or cond2: it'll exeute first condition true it'll not exeute second condition... second ccondition execution depends on first condition
if(10<20) | (10+"Hitu"=="10Hitu"):
    print("Answer is right")
else:
    print("Answer is wrong")

#OR example:
if(10<20) or (10+"Hitu"=="10Hitu"):
    print("Answer is right")
else:
    print("Answer is wrong")

#Assignment operator:
        # 1. Normal Assignment : =
        # 2. Augumented Assignment : *=, +=, -=, /=, %=

# Normal Assignment:
val = 10
print(val)

# Augumented Assignment:
# val += 10 --> in other lang val = val + 10... seond is val = val - 4... thrid is val = val - 2 and last val = val % 2
val += 10
val -= 4
val /= 2
val %= 2
print(val)

# In python increment and decrement (i++, i--, ++i, --i) operators are not there / python is not supporting 
# instead of that we've "Range function"

# Identity operators: is, is not : used for memory comparision : list, tuple, set.. it'll retur boolena answer (true or false)
value1 = 10
value2 = 10
print(value1 is value2)
print(value1 is not value2)

# Membership operator: in, not in : check data is available or not.. it'll also return boolean answer
data = [10,20,30,40]
print(10 in data)
print(100 in data)
print(10 not in data)