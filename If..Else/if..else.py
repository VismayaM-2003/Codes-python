#Conditions and if statement
#python supports usual logical conditions
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#These conditions most commonly used in "If Statements" and Loops
#"if statement" ---is written by using the if keyword.
a = 20
b = 790

if b > a:
    print("b is greater than a")
    
print("******************************************************************************")

#Indentation--If statement, without indentation (will raise an error)
"""
a = 20
b = 790
if b > a:
print("b is greater than a")

 File "demo_if_error.py", line 4
    print("b is greater than a")
        ^
IndentationError: expected an indented block

"""

#Elif----"if the previous conditions were not true, then  we can try this "Elif" condition".
c = 20
d = 46

if c > d:
    print("c is greater than d")
    
elif c < d:
    print("c is lesser than d")
    
print("**************************************************************************")

#Else--catches anything which isn't caught by the preceding conditions
a = 1000
b = 700

if b > a:
    print("b is greater than a") 
    
elif a == b:
    print("a is equals to b")
    
else:
    print("a is greater than b")
    
print("****************************************************************")

#we can also have an else without the elif
products = 100
workers = 200

if products > workers:
    print("products are greater than worksers")
    
else:
    print("products are lesser than workers")
    
print("******************************************************************")

#Short Hand If(one line if statement)
# If you have only one statement to execute, you can put it on the same line as the if statement.
x = 230
y = 479

if x < y: print("x is less than y")

print("*****************************************************")

#Short Hand If ... Else
#only one statement to execute, one for if, and one for else, you can put it all on the same line
a = 300
b = 10

print("YES") if a > b else print("NO")

print("*********************************************************")
#This technique is known as Ternary Operators, or Conditional Expressions.

#multiple else statements on the same line
x = 3000
y = 9000

print("Yes") if x > y else print("!=") if x!=y else print("No")

print("************************************************************")

#And--this keyword is a logical operator, and is used to combine conditional statements
a = 20
b = 9
c = 1000
if a > b and c > a:
  print("Both conditions are True")
  
else:
  print("False") 
  
print("***************************************************")

#Or keyword is a logical operator, and is used to combine conditional statements
x = 500
y = 1000
z = 300

if x > y or x > z:
  print("At least one of the conditions is True")
  
else:
 print("False")
 
print("************************************************************")

#Not keyword is a logical operator, and is used to reverse the result of the conditional statement
p = 80
q = 100

if not p > q:
    print("p is NOT greater than q")
    
print("***********************************************")

#Nested If---if statements inside if statements, this is called nested if statements
v = 100
if v > 10:
    print("v is Above 10")
    if v > 50:
        print("v is also Above 50")
        if v > 90:
           print("v is Above 90")
           
else:
    print("Not above 90")
    
print("***************************************************************")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
k = 33
l = 200

if l > k:
  pass

print("********************************************************************************")




