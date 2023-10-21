# Math
# Built in Math Functions
#The min() and max() functions can be used to find the lowest or highest value in an iterable:

# min()
num1 = min(4, 78, 2)  # Returns minimum value 2
# max()
num2 = max(4, 78, 2)  # Returns maximum value 78

print(num1)
print(num2)

print("*****************************")

#The abs() function returns the absolute (positive) value of the specified number:
# abs()
my_number = abs(-34.989)

print(my_number)    # 34.989

print("********************************")

#The pow(x, y) function returns the value of x to the power of y (xy).
# pow(x,y)
num_1 = pow(2,3)

print(num_1)    # 8

print("*************************************")

# The Math Module
#Python has also a built-in module called math, which extends the list of mathematical functions.
#To use it, you must import the math module:

import math   #when we imported we can start using methods and constants of the module.


# The math.sqrt() method-----returns the square root of a number:
import math

num1 = math.sqrt(81)   # 9.0

print(num1)

print("***************************************")

# The math.ceil() method--- rounds a number upwards to its nearest integer
import math

num2 = math.ceil(3.3)

print(num2)  # return number 4

print("*************************************")

# The math.floor() method--- rounds a number downwards to its nearest integer
import math

num3 = math.floor(3.6)

print(num3)  # return number 3

print("*************************************")

#The math.pi constant, returns the value of PI (3.14...):
import math
 
num4 = math.pi

print(num4)   #returns the pi value 3.14

print("************************************")