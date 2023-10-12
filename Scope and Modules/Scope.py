#Scope-A variable is only available from inside the region it is created. 

#Local Scope-A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def function():
    z = 20
    print(z)
    
function()

print("********************************************")

#Function Inside Function-the variable z is not available outside the function,but it is available for any function inside the function

def function():
    z = 200
    def innerfunction():
        print(z)
    innerfunction()
    
function()

print("***************************************************")

#Global Scope-A variable created outside of a function is global and can be used by anyone

Number = 100

def func():
    print(Number)
    
func()
print(Number)

print("***********************************************")

#Naming Variable
#if we use same variable name inside and outside of the function it will print the local scope and then print the global scope variable

a = 200

def myfunc():
    a = 10
    print(a)
    
myfunc()
print(a)

print("**********************************************")

#Global keyword--makes the variable global

a = 100
def name():
    global a
    a = "Vismaya"
    
name()
print(a)

print("************************************")