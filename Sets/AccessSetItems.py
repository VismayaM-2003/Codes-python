#Access Items
#cannot access items by referring to an index or a key.But can loop through the set items using a 
# for loop, or ask if a specified value is present in a set, by using the in keyword.
items={"Python","Language","C++",1,True}
for x in items:
    print(x)
print("*************************************************************")

#check the value present in the set
item1={"moon","sun","satellite"}
print("moon"  in item1)
print("****************************************************************")

#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
