#Accessing Items----by referring to its key name, inside square bracketsS
Access=	{
  "Name": "college",
  "Department": "Computer Science",
  "year": 2023
}
Value= Access["Department"]
print(Value)                  #value of the Department : Computer Science
print("**************************************************************")

#get()--get the value of the key
Access1=	{
  "Name": "HigherStudies",
  "Department": "Computer Science",
  "year": 2023
}
Value= Access1.get("Name")
print(Value)                #value of the "Name":"Ngm college"
print("*********************************************")

#Get Keys
#keys() method will return a list of all the keys in the dictionary
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
result= Table.keys()
print(result)         #Display the keys only
print("****************************************************************")

#Add a new item to the original dictionary
task={
     "TaskName":"Drawing",
     "Prize":"ColorsPack",
     "Amount":3000
}
result=task.keys()
print(result)   #before the change

task["Topic"]="Nature"
print(result)   #after the change
print("**************************************************************")

#Get Values
#values() method will return a list of all the values in the dictionary
Table=	{
  "Institution": "PI Tech",
  "Dept": "Computer Science",
  "year": 2023
}
result= Table.values()
print(result)         #Display the values only
print("*****************************************************************")

#Make a change in the original dictionary
Festival={
"Name": "Pongal",
"Month": "January",
"year": 2023
}
Answer= Festival.values()
print(Answer) #before the change

Festival["Month"]="December"
print(Answer) #after the change
print("***************************************************************************")

#Add a new item to the original dictionary
Festival={
"Name": "Pongal",
"Month": "January",
"year": 2023
}
Answer= Festival.values()
print(Answer) #before the change

Festival["Date"]="14.01.2023"
print(Answer) #after the change
print("********************************************************************************")

#Get Items
#items() method will return each item in a dictionary, as tuples in a list [()]
Access=	{
  "Name": "college",
  "Department": "Computer Science",
  "year": 2023
}
Value= Access.items()
print(Value)         
print("*******************************************************************************")     

#Make a change in the original dictionary
task1={
     "TaskName":"Drawing",
     "Prize":"ColorsPack",
     "Amount":3000
}
result1=task1.items()
print(result1)   #before the change

task1["Amount"]="500000"
print(result1)   #after the change
print("*******************************************************************************************************")

#Add a new item to the original dictionary
school={
    "classes":"1-12",
    "Sports":"playground"
}
output=school.items()
print(output) #before the change

school["Exam"]="Public Exam"
print(output) #after the change
print("*****************************************************")

#Check if Key Exists---use in keyword
Festival={
"Name": "Pongal",
"Month": "January",
"year": 2023
}
if "Month" in Festival:
    print("Yes, 'Month' is One of the key in this Dictionary")
print("**********************************************************************")

