#Dictionary--used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#written with curly brackets, and have keys and values
stud_details={
    "Name":"Vismaya",
    "Age":5,
    "year":2023
}
print(stud_details)
print("************************************************************************************")

#Dictionary Items--referred to by using the key name
details={
  "Name":"Govt",
  "State":"Tamilnadu",
  "year":2023
}
print(details["Name"])
print("*****************************************************************************************************")

#Duplicates Not Allowed----cannot have two items with the same key
About= {
  "StateName":"Kerala",
  "Language":"Malayalam",
  "year": 2000,
  "year": 2020
}
print(About)
print("***************************************************************************************")

#Dictionary Length---len()
stud_details={
    "Name":"Vismaya",
    "Age":5,
    "year":2023,
    "year":2020
}
print(len(stud_details))
print("*******************************************************************************************")

#Dictionary Items - Data Types
#The values in dictionary items can be of any data type
colors= {
  "name": "red",
  "url": False,
  "No_of_colors":50,
  "colors":["red", "white", "blue"]
}
print(colors)
print("*******************************************************************************************")

#type()
About= {
  "StateName":"Kerala",
  "Language":"Malayalam",
  "year": 2000,
  "year": 2020
}
print(type(About))
print("********************************************************************************")

#dict() Constructor
one=dict(name ="Ghandhi", age = 96,country = "India")
print(one) 
print("**************************************************************************")


