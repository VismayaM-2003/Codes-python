#sort list alphanumerically
#sort alphabetically
alpha=["Lemon","Mango","Apple","Watermelon","Banana",]
alpha.sort()
print(alpha)

print("******************************************************")

#sort numerically
number=[200,89,10,67,345,899]
number.sort()
print(number)

print("***********************************************")

#sort Descending alphabets
list=["anu","banu","chitra","darsha","suja"]
list.sort(reverse=True)
print(list)

print("******************************************************************")

#sort Descending numbers
list=[200,345,2,45,68,98,34,21,4,68]
list.sort(reverse=True)
print(list)

print("*********************************************************************************")

#customize sort function
def func(i):
  return abs(i-40)
numbers=[200,57,80,86,100]
numbers.sort(key=func)
print(numbers)

print("***********************************************************")

#case insensitive  sort---Uppercase first
cls=["first","second","Third","Forth"]
cls.sort()
print(cls)

print("**************************************************")

#lowercase first
cls=["Third","Forth","first","second"]
cls.sort(key=str.lower)
print(cls)

print("***************************************************")

#reverse()
numbers=[200,57,80,86,100]
numbers.reverse()
print(numbers)
