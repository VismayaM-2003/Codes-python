#Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Function Creation---function is defined using the def keyword
def my_function():
  print("Hello from a function")
  
#Calling a function
def my_function():
  print("Hello from a function") 

my_function() 

print("**************************************************************")

#Arguments--- specified after the function name, inside the parentheses. 
#we can add as many arguments as you want, just separate them with a comma.
#function with one argument (fname). When the function is called, 
# we pass along a first name, which is used inside the function to print the full name
def my_function(fname, Lname):
  print( fname+Lname + "Narayanan")

my_function("Sunitha ","Vismaya")
my_function("Ammu ","V")
my_function("Priya ","N")

print("**************************************************************************")

#Parameter / Arguments-- used for the same thing:information that are passed into a function

#In Functions
#A parameter is the variable listed inside the parentheses in the function definition.
#def my_function(fname):--(fname)=parameter
#An argument is the value that is sent to the function when it is called.
#my_function("Sunitha ")---("Sunitha")=argument

#Number of Arguments
#This function expects 2 arguments, and gets 2 arguments:

def func(fname, Lname):
  print(fname+" "+Lname)
func("Vismaya","Murugan")

print("*****************************************************************")

#If you try to call the function with 1 or 3 arguments, you will get an error
"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Achu")

Traceback (most recent call last):
  File "demo_function_args_error.py", line 4, in <module>
    my_function("Achu")
TypeError: my_function() missing 1 required positional argument: 'lname'
"""
#Arbitrary Arguments, *args
#If the number of arguments is unknown, add a * before the parameter name:
def function(*Friends):
  print("My best friend is " + Friends[5])
  
function("Duck", "Rabbit", "Lion", "Dog", "Cock", "Cat", "Parrot")

print("********************************************")

#Keyword Arguments-------send arguments with the key = value syntax.
def fruits(No1, No2, No3):
  print("My Favourite Fruit is " + No2)
  
fruits(No1 = "banana", No2 = "Apple", No3 = "Orange")

print("*************************************************")

#Arbitrary Keyword Arguments, **kwargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name
def details(**student):
  print("Her age is " + student["age"])
  
details(fname = "Vismaya", Lname = "Murugan", age = "14", place = "pollachi")

print("************************************************")

#Default Parameter Value
#If we call the function without argument, it uses the default value:
def India(state="Tamilnadu"):
  print("He is from " + state)
  
India("Kerala")
India("Himachal") 
India()
India("Delhi")

print("*******************************************")

#Passing a List as an Argument
def table(sports):
  for i in sports:
    print(i)
    
food=["Dosa", "Idle", "Maggie"]
table(food)

print("*************************************")

#Return Values--To let a function return a value, use the return statement
def maths(a):
  return 2 * a

print(maths(10))
print(maths(20))
print(maths(30))

print("******************************************")

#pass Statement
def study():
  pass

print("*************************************")


#doubt
"""
#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""





