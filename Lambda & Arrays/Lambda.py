#Lambda is a small anonymous function,take any number of arguments, but can only have one expression.
#Syntax-----lambda arguments : expression(expression is executed and the result is returned)
a = lambda x: x + 20
print(a(30))

print("**************************************************")

#can take any number of arguments
i = lambda x, y, z: x * y - z
print(i(5,4,3))

print("*********************************************")

#summarize arguments
x = lambda a, b, c, d, e: a + b + c + d + e
print(x(5,2,3,1,2))

print("**************************************************")

z = lambda a, b, c, d, e, f, g: a * b - c + d / e - f + g
print(z(1,7,5,8,9,14,5))

print("******************************")

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def function(i):
    return lambda x: x + i

result = function(2)
print(result(22))

print("*************************************************")

#multiply
def func(a):
    return lambda i: i * a

tripler = func(3)
print(tripler(11))

print("***********************************")

#use the same function definition to make both functions, in the same program
def func(a):
    return lambda i: i * a

doubler = func(2)
tripler = func(3)

print(doubler(11))
print(tripler(11))

print("***************************************")


