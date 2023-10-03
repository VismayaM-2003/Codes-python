#Remove specified item
color=["Orange","Red","Yellow"]
color.remove("Red")
print(color)

print("*******************************************************************************************")

#2 items with same name remove() removes the 1st item
color=["blue","Orange","Red","Green","Yellow","Orange"]
color.remove("Orange")
print(color)

print("*******************************************************************************************")

#POP(indexnum)---remove specified index-
List=["Carrot","Onion","knife"]
List.pop(1)
print(List)

print("*******************************************************************************************")
 
#pop()--remove  the last item
numbers=["500","799","783","678"]
numbers.pop()
print(numbers)

print("*******************************************************************************************")

#del--remove specified index
python=["Popular","Easy","Understandable","1991"]
del python[2]
print(python)

print("*******************************************************************************************")

#del--remove list completely
Integer=["1","33","55","66","77"]
del Integer
print(Integer)#shows err bcaz we dlt the "Integer" list 

print("*******************************************************************************************")

#clear()-empties the list
detail=["Name","Age","Class","Number"]
detail.clear()
print(detail)



 



