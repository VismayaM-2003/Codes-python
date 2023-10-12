#Python For Loops
#For Loop-used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#we can execute a set of statements, once for each item in a list, tuple, set etc

States = ["Tamilnadu","Kerala","Karnadaka","Andhra"]

for i in States:
    print(i)
    
print("*****************************************************************************************")

#Looping Through a String--"String"
#Even strings are iterable objects, they contain a sequence of characters
for a in "PYTHON":
    print(a)
    
print("********************************************************************")

#break Statement
Sports = ["Cricket","Football","Hockey","Chess"]

for x in Sports:
    print(x)
    
    if x=="Hockey":
        break
      
print("*************************************************************************")

#break comes before the print 
Sports = ["Cricket","Football","Hockey","Chess"]

for x in Sports:
    if x=="Hockey":
        break
    print(x)
    
print("*********************************************************************")

#continue statement
numbers = [1,2,3,4,5,6,7,8,9,5,7,7,8,9,0]

for x in numbers:
  if x == 5:
    continue
  print(x) 
  
print("*********************************************************************")

#range()
for c in range(9):
  print(c)
  
print("************************************************************************")

#The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(3, 9),
# which means values from 3 to 9 (but not including 9) 
for i in range(3, 9):
  print("\n",i) 
  
print("*****************************************************************************")

#The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(10, 30, 5):
for x in range(10, 30, 5):
  print(x) 
  
print("***********************************************************************")

#Else in For Loop
# else keyword in a for loop specifies a block of code to be executed when the loop is finished
for z in range(10):
  print(z)
  
else:
  print("range of 10 is finished!")
  
print("***********************************************************************")

#else block will NOT be executed if the loop is stopped by a break statement
for v in range(10):
  
  if v == 4: break
  print(v)

else:
  print("This will not be executed")
  
print("********************************************************")

#Nested Loops(loop inside a loop)
#Print each places for every people
places = ["School","College","Office"]
people = ["children","Students","Workers"]

for a in places:
  for b in people:
    print(a,b)
    
print("****************************************************************")

#pass statement
for a in [1,2,3]:
  pass

print("*********************************************************")

squares = []

for i in range(10):
    squares.append(i**2)
    
print(squares)



  







