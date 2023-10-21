#String Format--format() method

rate = 50

purse = "The purse is {} dollars"

print(purse.format(rate))

print("******************************************************")

#Multiple  Values

quantity = 3

itemno = 567

price = 49.95

myorder = "I want {} pieces of item {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price)) 

print("*******************************************************************")

#Index Numbers

price = 49

place = "kannan store"

txt = "The purse price is {0} dollars bought form {1}"

print(txt.format(price,place))

print("****************************************************")

#Also, if you want to refer to the same value more than once, use the index number:

name = "Aishu"

age = 5

about_her = "Her name is {0}, and {0} interested in learning new technologies.."

print(about_her.format(name,age))

print("**********************************************")

#Named Indexes

candidate = "My name is {name} , I am from {place}."

print(candidate.format(name = "Anu", place = "Chennai"))