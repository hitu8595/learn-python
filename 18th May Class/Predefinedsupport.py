# C language predefined support ---- Header files (stdio.h) ----- Contains Functions (eg.. printf)
# Java lang predefined support ---- Packages (java.lang package) --- contains clasees, interfaces (eg.. system, string)
#Python lang predefined support ---- module(OS) --- contains classes, variables, functions (eg..remove(), mkdir())

#To see modules present in python use "help" command
print(help("modules"))

#To see what print does in python use "help" command
print(help("print"))

#TO see the data of modules use "dir"(directory) function
import os
print(dir(os))

import keyword
print(dir(keyword))

#Output: ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'iskeyword', 'kwlist']

# The data starts with __ (double underscore) & ends with 2 underscores is calles as  "magic functions"
#Afeter the magic  function we've "variables & functions"
#Before magic function we've "classes"

# "iskeyword" is to check whether is keyword or not
import keyword
print(keyword.iskeyword("print"))

#Note: module name all characters must be lower case
# variables does't contain paranthases
# Functions contains paranthases