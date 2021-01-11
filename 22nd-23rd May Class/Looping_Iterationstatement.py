# 2. Looping- Iterational statement:
# syntax: for temp-var in iteration_data:
#             print("gkgkj")

# range() function - used to repeat the loop... range(4)--> it'll take 0,1,2,3.. automatically increament +1
# range(2,7): 2 3 4 5 6 (last value will be excluded)
# range(start, stoop, step)...range(2,8,2): menaing 2-8 by stepping 2... asnwer: 2 4 6 (8 is excluded)

for x in range(10):
    print("GM", x)

for y in range(2,7):
    print("GE", y)

for z in range(2,8,3):
    print("GN", z)

val=3
for b in range(val):
    print("GA", b)

#printing even num from 1,100:
for a in range(1,21):
    if a%2==0:
        print("Even Numbers are", a)

# By default printing will be vertically... if we want to print horizantally
for c in range(1,11):
    print(c, end=" ")

#input function: it'll take by default string
#break vs continue: break will stop the execution after certain limit of range.... continue will skip that particular number and will continue till the range finish
num = int(input("Boys enter the number"))
for d in range(10):
    if d==num:
        break
    print(d)

num = int(input("Girls enter the number"))
for d in range(10):
    if d==num:
        continue
    print(d)

#Range function decrement will not happen automatically but inrement by 1 will automatic
for z in range(7,2,-1):
    print("GM", z)
for w in range(8,3,-3):
    print("GE", w)

#Negative indexing: lowest to highest means increment
for y in range(-8,-3):
    print("Hello", y)
for p in range(-8,-3,2):
    print("Hello, GM", p)

#Negative Indexxing: highest to lowest means decrement and will not it automaticaly we have to provide 3rd value
for m in range(-2,-8,-3):
    print("GEEE..", m)

#iterating name using for loop / the loop is iterated with every charater
name = "Hitu"
for x in name:
    print(x)

#stop the execution when t occured:
name = "Hitasvi"
for x in name:
    if x=='t':
        break
    print(x)

#sum of even numbers from 1-100:
# without sum() function:
total = 0
for x in range(0,101,2):
    total += x
print("Result...",total)

#with sum() function
print("Result...",sum(range(0,101,2)))