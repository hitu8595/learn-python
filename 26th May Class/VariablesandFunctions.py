# #variables : used to store the data and it is a fixed memory locations
#            # - every variable contains type
#            # python works with both functions based (ex. C lang) and object based (ex. java lang)
#         # There are three types of variables at function bases:
#           # 1. local variables
#           # 2. global variables
#           # 3. non-local variables
#         # 2 kind of variables with object based at class level:
#           # 1. instant variables
#           # 2. static variables

# #function : it is used to write the block of python code
#         # we can call the function in app wherever we want
#         # declare the function using def keyword
#         # main objective of the function is reuse the code

#         # it contains 3 parts:
#            # 1. function declaration
#            # 2. function body // definition // implementation
#            # 3. function call
        
#         # syntax: 
#             #def func_name(args_list):
#              #   body(logics)

# #example1: function declaration
# def wish(name):
#   print("Good Morning...",name)

# def game():
#   print("Hello....")

# #function call:
# wish("Hitu")
# game()

# #Example2: local variables : variables inside the function or in the function or (function arguments) both are local variables
#           # the scope of the local variables is with in the function and we can not access outside of the function
# def wish2():
#   name2 = "Hitu"
#   print("Good Morning...",name2)

# def add(num1,num2):
#   print(num1+num2)

# #function call
# wish2()
# add(10,20)

# #example3: global variable: the scope of this variables is all function can use the declared variables
# uname = "Hitu"   #global variables
# def wish1():
#   print("Good Morning...",uname)

# def fname():
#   print("GE>...",uname)

# #function call
# wish1()
# fname()

# #example4: local and global variables with diferent names
# number1,number2 = 10,20
# def add1(val1,val2):
#   print(val1+val2)
#   print(number1+number2)

# def mul(val1,val2):
#   print(val1*val2)
#   print(number1*number2)

# #function call:
# add1(100,200)
# mul(4,5)

# #example 5: local and global variables with same names:
# number4,number5 = 10,20
# def add2(number4,number5):
#   print(number4+number5)

# def multi(number4,number5):
#   print(number4*number5)

# #function call:
# add2(number4,number5) #accessing global variables value
# add2(30,40) #accessng local variables value
# multi(number4,number5)
# multi(30,40)

# #example 6: inside the functon  want to declare global varable so use global inside the function

# def studentname():
#   global name4
#   name4 = "Hitu"
#   print("GM....",name4)

# studentname()
# print("GE....",name4)

# #imp :   #exampke7: want to change the global datato local data/name use global keyword inside the function

# username = "Mom"
# def namechange():
#   global username
#   username = "Daddy"
#   print("GM.....",username)

# namechange()
# print("GE...",username)

# #example8:
# def a_fun():
#   global foo
#   foo = 'A'

# def b_fun():
#   global foo
#   foo = 'B'

# #function calling
# b_fun()
# a_fun()
# print(foo)

#example9:
a,b,x,y = 1,15,3,4
def foo2(x,y):
  a = 42
  x,y = y,x
  b = 33
  print(a,b,x,y)

#function calling:
foo2(17,4)
print(a,b,x,y)