#To check the keywords use "kwlist" variable
#"kwlist" is a variable present in "keyword" module
#Python 2.7 version and 3.8 version keywords are different... currently in OP we are getting 3.8 keywords:
#when we use predefined module we've to import that module

import keyword
print(keyword.kwlist)

#In python 2.x version "print" is keyword so, paranthases not required to print he data
#Example: print "Hello world"
#In 3.x verison "print" is a function so, paranthases required