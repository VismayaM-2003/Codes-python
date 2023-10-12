#Loop Dictionary
#Print all key names in the dictionary, one by one
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
for x in table:
    print(x)
print("************************************************************************")

#Print all values in the dictionary, one by one
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
for x in table:
    print(table[x])  
print("**********************************************")

#also use values() method
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
for x in table.values():
    print(x)  
print("**********************************************")

#use keys() to print only the key names
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
for x in table.keys():
    print(x)  
print("**********************************************")

#items()
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
for x,y in table.items():
    print(x,y)  
print("**********************************************")









