#Add Items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
numbers={10,20,30,40,50}
numbers.add("Numeric Values")
print(numbers)
print("***********************************************")

#Add Sets
#add items from another set into the current set, use the update() method.
test1={12,45,67,34,56}
test2={"Moon","Sun","Sky"}
test1.update(test2)
print(test1)
print("******************************************************************")

#Add Any Iterable
#we can Add elements of a list to at set
new1={"r","g","b"}
new2=["Asia","Arabia","Dubai","Jappan"]
new1.update(new2)
print(new1)
print("***************************************************************")
