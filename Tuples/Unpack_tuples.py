#Unpack tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
print("Packing a tuple")
numeric=(1,2,3,4,5,6,7)
print(numeric)
#we are also allowed to extract the values back into variables. This is called "unpacking"
print("Unpacking a tuple")
task=("Jump","Swim","Run")
(height,Water,surface)=task
print(height)
print(Water)
print(surface)
print("***************************************************************************")

#Using Asterisk*---used to print remaining values
task=("Jump","Swim","Run","walk","fly","Read")
(height,*Water,surface)=task
print(height)
print(Water)
print(surface)
