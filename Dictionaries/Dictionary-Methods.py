#Dictionary Methods
#clear()	Removes all the elements from the dictionary
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
Table.clear()
print(Table)
print("***************************************************************************")

#copy()	Returns a copy of the dictionary
shop={
    "products":"Toys",
    "Rates":200
}
result=shop.copy()
print(result)
print("*****************************************************************")

#fromkeys()	Returns a dictionary with the specified keys and value
one= ('key1', 'key2', 'key3')
two= 10
three= dict.fromkeys(one,two)
print(three)
print("***************************************************************")

#get()	Returns the value of the specified key
Access1=	{
  "Name": "HigherStudies",
  "Department": "Computer Science",
  "year": 2023
}
Value= Access1.get("Name")
print(Value)                #value of the "Name":"Ngm college"
print("**************************************************************")

#items()	Returns a list containing a tuple for each key value pair
Access=	{
  "Name": "college",
  "Department": "Computer Science",
  "year": 2023
}
Value= Access.items()
print(Value)         
print("*******************************************************************************")     

#keys()	Returns a list containing the dictionary's keys
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
result= Table.keys()
print(result)         #Display the keys only
print("****************************************************************")

#pop()	Removes the element with the specified key
task1={
     "TaskName":"Drawing",
     "Prize":"ColorsPack",
     "Amount":3000
}
task1.pop("Amount")
print(task1)
print("*********************************************************")

#popitem()	Removes the last inserted key-value pair
Festival={
"Name": "Pongal",
"Month": "January",
"year": 2023
}
Festival.popitem()
print(Festival)
print("****************************************")


#setdefault()	
# Returns the value of the specified key. 
shop= {
  "front": "bill",
  "middle": "process",
  "year": 1964
}
x = shop.setdefault("middle", "workers")
print(x)
print("*********************************************************")

## If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)
print("*********************************************************************")




#update()	Updates the dictionary with the specified key-value pairs
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
table.update({"Hobbies":"Drawing"})
print(table)
print("********************************************************************************")

#values()	Returns a list of all the values in the dictionary
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
result= Table.values()
print(result)         #Display the values only
print("*****************************************************************")