#Change Values--specific item by referring to its key name
task1={
     "TaskName":"Drawing",
     "Prize":"ColorsPack",
     "Amount":3000
}
task1["Amount"]=500000
print(task1)   
print("*****************************************************************************************")

#Update Dictionary
#update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
table={
    "Name":"Vismaya",
    "Age":3,
    "year":2023
}
table.update({"year":2025})
print(table)
print("********************************************************************************")
