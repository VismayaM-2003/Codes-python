#Polymorphism--means "many forms", and in programming it refers to methods/functions/operators 
# with the same name that can be executed on many objects or classes.

#Function Polymorphism----len() function
#string--number of characters
a = "Welcome to python"
print(len(a))

print("***************************************")

#Tuple--number of items in the tuple
task = ("net","flight","cricket","cat","dog")
print(len(task))

print("**********************************")

#Dictionaries--number of key/value pairs 
details = {
    
    "name":"Vismaya",
    "age":12,
    "year":2023
    
}

print(len(details))

print("***************************************")

#Class Polymorphism
#move()--polymorphism
class firstyear:
    def __init__(self,strength,shift):
        self.strength = strength
        self.shift = shift
        
    def year(self):
        print("2021")

class secondyear:
    def __init__(self,strength,shift):
        self.strength = strength
        self.shift = shift
        
    def year(self):
        print("2022")
        
class thirdyear:
    def __init__(self,strength,shift):
        self.strength = strength
        self.shift = shift
        
    def year(self):
        print("2023")
        
first = firstyear("100","1-shift")      #create a firstyear class
second = secondyear("70","2-shift")     #create a secondyear class
third = thirdyear("50","1-shift")       #create a thirdyear class

for x in(first,second,third):
    x.year()
    
print("***********************************************")

#Inheritance Class Polymorphism
class college:
    def __init__(self,strength,shift):
        self.strength = strength
        self.shift = shift
        
    def year(self):
        print("2021-2023")
        
class firstyear(college):
  pass

class secondyear(college):
    def year(self):
        print("2022")
        
class thirdyear(college):
    def year(self):
        print("2023")
        
first = firstyear("100","1-shift")   #create a firstyear object
second = secondyear("70","2-shift")  #create a secondyear object
third = thirdyear("50","1-shift")    #create a thirdyear object

for x in(first,second,third):
    print(x.strength)
    print(x.shift)
    x.year()