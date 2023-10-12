#Remove item---use the remove(), or the discard() method

#remove()
products={"Vegetables","Juice","Toys"}
products.remove("Juice")
print(products)
print("*******************************************************************")

#discard()
items={"Bottles","Glasses","Shoes"}
items.discard("Shoes")
print(items)
print("****************************************************************")

#pop()
#we can use the pop() method to remove an item, but this method will remove a random item,
#so you cannot be sure what item that gets removed.
values={"Vismaya","Have","completed","her","college"}
value1=values.pop()
print(value1)    #removed item
print(values)    #the  set  after removal
print("**************************************************************************")

#clear()-- method empties the set
item2={"Sunday","Monday","Tuesday"}
item2.clear()
print(item2)
print("**********************************************")

#del keyword will delete the set completely
item2={"Sunday","Monday","Tuesday"}
del item2
print(item2)

