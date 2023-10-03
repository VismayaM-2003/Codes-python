#List comprehension
stud_Names=["vismaya","sumi","malar","sandy","prabha"]
new_names=[]

for i in stud_Names:
    if "s" in i:
      new_names.append(i)

print(new_names)

print("*******************************************************************************")

#only one line of the code
stud_Names=["vismaya","sumi","malar","sandy","prabha"]
new_names=[i for i in stud_Names if "s" in i]
print(new_names)

#syntax---newlist = [expression for item in iterable if condition == True]

print("********************************************************************************************")

#condition
stud_Names=["vismaya","sumi","malar","sandy","prabha"]
new_names=[i for i in stud_Names if i!="vismaya"]
print(new_names)

print("*********************************************************************************************")

#without condition
names=["malu","biju","achu","unni"]
list=[x for x in names]
print(list)

print("**************************************************************************************************")

#Iterable
#using range() for iterable
const=[x for x in range(100)]
print(const)

print("**********************************************************************************************")

#with condition
const=[x for x in range(100) if x<50]
print(const)

print("***********************************************************************")

#Expression
team=["football","cricket","chess","hockey"]
new_team=[x.upper() for x in team]
print(new_team)

print("*********************************************************")

#same example filled with same name
team=["football","cricket","chess","hockey"]
new_team=['Sports' for x in team]
print(new_team)

print("******************************************************")

#if else condition
colors=["orange","violet","pink","yelow"]
rainbow=[x if x!="violet" else "Green" for x in colors]
print(rainbow)
     



