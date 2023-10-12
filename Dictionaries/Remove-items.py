#Removing items
#pop()--method removes the item with the specified key name
task1={
     "TaskName":"Drawing",
     "Prize":"ColorsPack",
     "Amount":3000
}
task1.pop("Amount")
print(task1)
print("*********************************************************")

#popitem()--method removes the last inserted item
Festival={
"Name": "Pongal",
"Month": "January",
"year": 2023
}
Festival.popitem()
print(Festival)
print("****************************************")

#del--removes the item with the specified key name
Pack= {
  "Group": "Python",
  "Members": 8,
  "year": 2024
}
del Pack["Group"]
print(Pack)
print("********************************************************************************")

#Clear()
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
Table.clear()
print(Table)

