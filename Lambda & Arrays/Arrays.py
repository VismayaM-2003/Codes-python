#Arrays are used to store multiple values in one single variable:
flowers = ["Rose", "Sunflower", "Jasmine", "Lotus"]
print(flowers)

print("**********************************")

#An array is a special variable, which can hold more than one value at a time.
#access the values by referring to an index number.

#Access the Elements of an Array
flowers = ["Rose", "Sunflower", "Jasmine", "Lotus"]
i = flowers[2]
print(i)

print("******************************************")

#Modify the value
colors = ["red", "blue", "white"]
colors[1] = "Black"
print(colors)

print("***********************************")

#length() array
Numbers = [12, 13, 24, 34, 55, 67]
result = len(Numbers)
print(result)

print("************************************")

#Looping Array elements
india = ["Tamilnadu", "kerala", "Andhra"]
for i in india:
    print(i)
    
print("**************************")

#Adding array elementts--append()
table1 = ["college", "school", "office"]
table1.append("company")
print(table1)

print("******************************************")

#Removing Array Elements--pop()
building = ["floor-1", "officeroom", "floor-2", "floor-3"]
building.pop(1)
print(building)

print("************************************")

#remove()
library = ["English", "Grammers", "Poems", "Compositions", "Stories"]
library.remove("English")
print(library)

print("*************************************")

#Array Methods
#append()	Adds an element at the end of the list
table1 = ["college", "school", "office"]
table1.append("company")
print(table1)

print("****************************************************")

#clear()	Removes all the elements from the list
task = ["singing", "Dancing", "Swimming"]
task.clear()
print(task)

print("****************************************************")

#copy()	Returns a copy of the list
Numbers = [10, 20, 30, 40, 50]
Numbers.copy()
print(Numbers)

print("****************************************************")

#count()	Returns the number of elements with the specified value
rainbow = ["red", "violet", "indico", "yellow", "green", "red", "blue", "red"]
i = rainbow.count("red")
print(i)

print("****************************************************")

#extend()	Add the elements of a list (or any iterable), to the end of the current list
table1 = ["Apple", "carrot", "banana"]
table2 = [123, 679, 900, 653]
table1.extend(table2)
print(table1)

print("****************************************************")

#index()	Returns the index of the first element with the specified value
names = ["Anu", "beeshma", "Chithu", "dharshu"]
i = names.index("beeshma")
print(i)

print("****************************************************")

#insert()	Adds an element at the specified position
pack = ["net", "ball", "puppy", "cat"]
pack.insert(2,"Peacock")
print(pack)

print("****************************************************")

#pop()	Removes the element at the specified position
building = ["floor-1", "officeroom", "floor-2", "floor-3"]
building.pop(1)
print(building)

print("****************************************************")

#remove()	Removes the first item with the specified value
library = ["English", "Grammers", "Poems", "Compositions", "Stories"]
library.remove("English")
print(library)

print("****************************************************")

#reverse()	Reverses the order of the list
student = ["Vismaya", "is", "name", "My"]
student.reverse()
print(student)

print("****************************************************")

#sort()	Sorts the list
order = ["Yellow", "Lion", "Apple", "Vismaya", "Python", "Banana"]
order.sort()
print(order)

print("****************************************************")



