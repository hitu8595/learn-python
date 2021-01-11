#4 different type of data types int float, string, bool (True"1" False("0"))
val1 = 10
val2 = 20.5
val3 = "Hitu"
val4 = True

#To check the type of data use "type" function
print(type(val1))
print(type(val2))
print(type(val3))
print(type(val4))

#Another Way
eid, ename, esalary, status = 12, "Hitu", 10000.50, True
print(eid)
print(ename)
print(esalary)
print(status)

#complex numbers: real and imaginary values will give answers in decimal or string format
num1 = 1+2j # real number is 1. & imag=2.0
num2 = 4j   #real is 0.0 and imag=4.0

print(num1)
print(num2)
print(num1.real)
print(num2.imag)

num2.real=10  #Attributeerroe: readonly attribute