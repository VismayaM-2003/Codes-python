#Classes and Objects.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class--use the keyword class.

class heading:
    x = 5
print(heading)

print("*************************************")

#create an object

class stud:
    x = 20
    
a1 = stud()
print(a1.x)

print("***************************************************************")

#__init__() function

class stud:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x = stud("Sheela", 36)

print(x.name)
print(x.age)

print("************************************")

#__str__() Function--controls what should be returned when the class object is represented as a string.
#__str__() function is not set, the string representation of the object is returned

#string representation of an object WITHOUT the __str__() function:
class stud:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x = stud("Vismaya",5)

print(x)

print("**********************************************")

#The string representation of an object WITH the __str__() function:
class color:
  def __init__(self, name, rate):
    self.name = name
    self.rate = rate

  def __str__(self):
    return f"{self.name}({self.rate})"    

x= color("Blue", 20)

print(x)

print("******************************************************************")

#Objecct Methods
#Methods in objects are functions that belong to the object

class school:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    
  def func(self):
    print("I am " + self.name)
    
x = school("Jeni",3098)
x.func()

print("**********************************************")

#self parameter--used to access variables that belong to the class.
# it has to be the first parameter of any function in the class
#we can use words myhome and xyz instead of self 
class college:
  def __init__(myhome, name, age):
    myhome.name = name
    myhome.age = age

  def myfunc(xyz):
    print("My name is " + xyz.name)

i = college("Vismaya", 36)
i.myfunc()

print("**********************************************************")

#Modify Object Properties
class college:
    def __init__(self,dept,year):
        self.dept = dept
        self.year = year
        
    def func(self):
      print("I have completed my degree in " + self.dept)
      
i = college("Computer Science",2023)
i.year = 2024
print(i.year)

print("*************************************")

#Delete Object Properties--del keyword
class python:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    
  def function(self):
    print("Welcome everyone to " + self.name)
    
a = python("Python",1991)
"""
del a.year
Traceback (most recent call last):
  File "c:\python\Class and objects\class_obj.py", line 110, in <module>
    print(a.year)
          ^^^^^^
AttributeError: 'python' object has no attribute 'year'
"""
a.function()
print(a.year)

print("*******************************")

#Delete Objects
class home:
  def __init__(self,place,district):
    self.place = place
    self.district = district
    
  def myfunc(self):
    print("I am living in " + self.place)
    
a = home("Pollachi","Coimbatore")
a.myfunc()
"""
del a
Traceback (most recent call last):
  File "c:\python\Class and objects\class_obj.py", line 131, in <module>
    print(a)
          ^
NameError: name 'a' is not defined. Did you mean: 'a1'?
"""
print(a)

print("**************************************************")

#Pass Statement
class MyApp:
  pass


  
    
  




print("*************************************")

