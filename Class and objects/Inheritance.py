#Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Create a Parent Class
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)

x = Family("Sundharam "," Saraswathi")
x.printfamily()

print("********************************************")

#Create a Child Class
#Create a class named parent, which will inherit the properties and methods from the Family class
class parent(Family):
    pass

print("*************************************************")

#Now the parent class has the same properties and methods as the Family class.
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)
        
class parent(Family):
    pass

x = parent("Murugan ","Vijiyasree")
x.printfamily()

print("*********************************************")

#Add the __init__() Function--to the child class.
"""class parent:
    def __init__(self,dad,mom):
        self.dad = dad
        self.mom = mom............."""
        
#When you add the __init__() function, thechild class will no longer inherit the parent's __init__() function.

#To keep the inheritance of the parent's __init__() function,add a call to the parent's __init__() function:
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
    
    def printfamily(self):
        print(self.grandpa,self.grandma)
    
class parent(Family):
    
    def __init__(self,grandpa,grandma):
        Family.__init__(self,grandpa,grandma)
        
x = parent("Jack" , "Laura")
x.printfamily()

print("************************************")

#super()--make the child class inherit all the methods and properties from its parent:
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)

class parent(Family):
    def __init__(self,grandpa,grandma):
        super().__init__(grandpa,grandma)
        
x = parent("Sanju","Ammu")
x.printfamily()

print("****************************************")

#Add Properties
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)

class parent(Family):
    
    def __init__(self,grandpa,grandma):
        super().__init__(grandpa,grandma)
        self.birthmonth="May"
        
x = parent("Sanju","Ammu")

x.printfamily()
print(x.birthmonth)

print("****************************************")

#add a month
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)

class parent(Family):
    def __init__(self,grandpa,grandma,month):
        super().__init__(grandpa,grandma)
        self.birthmonth = month
        
x = parent("Sanju","Ammu","May")

x.printfamily()
print(x.birthmonth)

print("****************************************")

#Add a Method
class Family:
    
    def __init__(self,grandpa,grandma):
        self.grandpa = grandpa
        self.grandma = grandma
        
    def printfamily(self):
        print(self.grandpa,self.grandma)

class parent(Family):
    
    def __init__(self,grandpa,grandma,month):
        super().__init__(grandpa,grandma)
        self.birthmonth = month
        
    def welcome(self):
        print("Welcome",self.grandpa,self.grandma,"to the",self.birthmonth,"Month")
        
x = parent("Sanju","Ammu","May")
x.welcome()

print("****************************************")

        

