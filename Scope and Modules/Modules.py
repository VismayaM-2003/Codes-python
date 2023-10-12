# Modules-A file containing a set of functions you want to include in your application.

#Create a Module--save code in a file named mymodule.py

#Usa a module-import statement.
import mymodule

mymodule.greet("Vismaya")

print("***********************************")

#Variables in Module.
import mymodule

x = mymodule.college["dept"]
print(x)

print("********************************")

#Naming a Module--Renaming a module using(as keyword).
import mymodule as mod

a = mod.college["year"]
print(a)

print("****************************************")

#Built-in Modules
import platform

new_1 = platform.system()
print(new_1)

print("*********************************")

#Using the dir() Function.
#To list all the function names(or variable names) in a module.
import platform

result = dir(platform)
print(result)

print("***************************")


#Import from Module.
#from keyword-You can choose to import only parts from a module, by using the from keyword.

#The module named mymodule has one function and one dictionary.

#Import only the college dictionary from the module.
from mymodule import college

print (college["dept"])
