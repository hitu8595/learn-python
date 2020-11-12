#To print 10***20***30
a,b,c = 10,20,30

# case1 - not recommended
print(f"{a}***{b}***{c}")

#case2 - recommened (by using separator).. we are giving separator explicitly
print(a,b,c,sep="***")
print(a,b,c,sep="$$$")
print(a,b,c,sep="%%%")

#Default separator is space
print(a,b,c)

#Print statement - after printing anything it'll(control) go to new line.. observe in o/p console
print("GM")
#To avoid the above consequence... we can use 'end=""'
print("GN", end="")

#To see the implementation of function use "help()" funtion
print(help("print"))
print(help("modules"))