eid, ename, esalary, status = 12, "Hitu", 10000.50, True

#Printing in one line
print(eid, ename, esalary, status)

#Printing extra values in line
print("Emp Id=", eid)
print("Emp Name=", ename)
print("Emp Salary=", esalary)
print("Emp Status=", status)

#Printing extra values in one line... we can format data in 3 ways
#By using %
print("Emp Id = %d Emp Name = %s Emp Salary = %f" %(eid, ename, esalary))
#By using {} - reommended
print("Emp Id = {} Emp Name = {} Emp Salary = {}".format(eid, ename, esalary))
print("Emp Id = {0} Emp Name = {1} Emp Salary = {2}".format(eid, ename, esalary))
#By using f (formating) - reommended and most used 
print(f"Emp Id = {eid} Emp Name = {ename} Emp Salary = {esalary}")

#To Print middle charater with special charater we use \...\ (back slace)/ escape sequence character
print("Hello Hitu Here")
print("Hello \"Hitu\" Here")
print("Hello \\Hitu\\ Here")
print("Hello \'Hitu\' Here")
#For 1 tabbing \t...\t
#For 2 tabbing \t\t....\t\t
print("Hello\tHitu\tHere")
#For new line \n..\n
print("Hello\nHitu\nHere")

#If our data is in double quote and we want to type something in ''.. no need to use escape character and vice cersa
print("Hello 'Hitu' GM")
print('Hello "Hitu" GM')
print("""Hello "Hitu" GM 'GN'""")