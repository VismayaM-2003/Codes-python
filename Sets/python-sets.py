#Sets
#used  to store multiple items in one variable
#unordered, unchangeable*, and unindexed.
#written with curly brackets.
numbers={"one","two","three","four","five"}
print(numbers)
print("*********************************************************************************")

#Duplicates not allowed
class1={"Red","Blue","Orange","Violet","Blue","Green","Blue"}
print(class1)   
print("***************************************************************************")

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
task={"Laptop","Monitor",True,"Keyboard",1,2}
print(task)
print("**************************************************************")

#Get the length of a set
test={"Apple","Juice",1,2,True,0,False,"shop"}
print(len(test))
print("***********************************************************************************")

#Set Items-Data Types
test1={"Aksha","Biju","Chandhrika","Dharshu"}
test2={1,34,56,35,78}
test3={True,False,False,True}
print(test1)
print(test2)
print(test3)

Test={"Aksha",12,True,"robot",89,False}
print(Test)
print("*******************************************************************************************")

#Type()
task={"Aksha",12,True,"robot",89,False}
print(type(task))
print("*************************************************************************")

#set() constructor
table=set(("Vismaya","Anu",23,False))
print(table)
print("***********************************************************************")


