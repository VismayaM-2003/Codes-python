#Set Methods
# add()--Adds an element to the set
one={100,200,300}
one.add("Hello")
print(one)
print("***********************************************************************")

# clear()--Removes all the elements from the set
item2={"Sunday","Monday","Tuesday"}
item2.clear()
print(item2)
print("***********************************************************************")

# copy()--Returns a copy of the set
task={"hello",True,False,20,67}
task1=task.copy()
print(task1)
print("***********************************************************************")

# difference()--Returns a set containing the difference between two or more sets
one={"Hello","World","Python"}
two={"Python",123,567}
three=one.difference(two)
print(three)
print("***********************************************************************")

"""The difference_update() method is different from the difference() method, 
because the difference() method returns a new set, without the unwanted items, 
and the difference_update() method removes the unwanted items from the original set."""


# difference_update()--Removes the items in this set that are also included in another, specified set
four={100,500,689,"python","Java"}
five={100,"C"}
four.difference_update(five)
print(four)
print("***********************************************************************")

# discard()	--Remove the specified item
items={"Bottles","Glasses","Shoes"}
items.discard("Shoes")
print(items)
print("***********************************************************************")

# intersection()--	Returns a set, that is the intersection of two other sets
number1={100,200,300,400,500}
number2={"Strawberry","Banana","Apple",400}
number3=number1.intersection(number2)
print(number3)                          #{400}

item1= {"a", "b", "c"}
item2= {"c", "d", "e"}
item3= {"f", "g", "c"}
result = item1.intersection(item2, item3)
print(result)                               #c
print("***********************************************************************")

# intersection_update()	--Removes the items in this set that are not present in other, specified set(s)
one={"Green","Blue","Red","Violet"}
two={"Blue",67,True,"Yellow"}           #{"Blue"}
one.intersection_update(two)
print(one)
print("***********************************************************************")

# isdisjoint()	--Returns whether two sets have a intersection or not
product_list1={"Apple","Orange"}
product_list2={120,459}
product_list3=product_list1.isdisjoint(product_list2)
print(product_list3)    #True

product1={"Apple","Orange"}
product2={120,459,"Apple","Orange"}
product3=product1.isdisjoint(product2)
print(product3)             #False

print("***********************************************************************")

# issubset()--Returns whether another set contains this set or not
numbers1={1,2,3,5}
numbers2={"a","b","c","d",1,2,3,5}
numbers=numbers1.issubset(numbers2)
print(numbers)

Value1={1,2,3,5}
Value2={"a","b","c","d"}
Values=Value1.issubset(Value2)
print(Values)
print("***********************************************************************")

# issuperset()--Returns whether this set contains another set or not
test1={"C","D",1,2,3,4,5,}
test2={"A","B","C","D"}
test=test1.issuperset(test2)
print(test)

number1={1,2,3,4,"Hello","python"}
number2={1,2,3,4}
numbers=number1.issuperset(number2)
print(numbers)
print("***********************************************************************")

# pop()	--Removes an element from the set
values={"Vismaya","Have","completed","her","college"}
value1=values.pop()
print(value1)    #removed item
print(values)    #the  set  after removal
print("***********************************************************************")

# remove()--	Removes the specified element
products={"Vegetables","Juice","Toys"}
products.remove("Juice")
print(products)
print("***********************************************************************")

# symmetric_difference()--	Returns a set with the symmetric differences of two sets
one={"Renu","Beeshma","vismaya"}
two={"Beeshma","Renu",111,564}
three=one.symmetric_difference(two)
print(three)
print("***********************************************************************")

# symmetric_difference_update()	--inserts the symmetric differences from this set and another
task1={"Green","Blue","Red","Violet"}
task2={"Blue",67,True,"Yellow"}           
task1.symmetric_difference_update(task2)
print(task1)
print("***********************************************************************")

# union()--Return a set containing the union of sets
first={"Shift","Tab","Space"}
second={"day","after","night"}
third=first.union(second)
print(third)
print("***********************************************************************")

# update()--Update the set with the union of this set and others
table1={1,3,45,6,32,67}
table2={"RAinbow","Falls","Nature","Mountain"}
table1.update(table2)
print(table1)
print("***********************************************************************")