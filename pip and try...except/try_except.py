#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.

#Exception Handling
#try
try:
    print(name)    #The try block will generate an error, because namee is not defined:
    
except:
    print("An Exception occured")

print("**********************************************")

#Many Exceptions
try:
    print(name)   #The try block will generate a NameError, because name is not defined:
    
except NameError:
    print("Variable name is not defined")

except:
    print("Something went wrong!")
    
print("**************************************")

#Else--to define a block of code to be executed if no errors were raised:

try:
  print("Welcome Home...")
  
except:
  print("Something went wrong")
  
else:
  print("Nothing went wrong")

print("**************************************************************")

#Finally-- if specified, will be executed regardless if the try block raises an error or not.

try:
  print(name)
  
except:
  print("Something went wrong")
  
finally:   #The finally block gets executed no matter if the try block raises any errors or not:
  print("The 'try except' is finished")

print("********************************************************")

#Raise an Exception
#You can define what kind of error to raise, and the text to print to the user.

my_value = 234

if not type(my_value) is str:
    
    raise TypeError("only strings are allowed")

print("****************************************")


#To throw (or raise) an exception, use the raise keyword.
"""number = -23

if number < 0:
    raise Exception("Sorry.. No numbers below 0")
"""

"""
raise Exception("Sorry.. No numbers below 0")
Exception: Sorry.. No numbers below 0
"""

print("**************************************")