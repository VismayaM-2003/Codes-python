#Join two sets
#union()--returns a new set with all items from both sets
first={"Shift","Tab","Space"}
second={"day","after","night"}
third=first.union(second)
print(third)
print("**********************************************************************")

#update() --- inserts the items in set2 into set1
table1={1,3,45,6,32,67}
table2={"RAinbow","Falls","Nature","Mountain"}
table1.update(table2)
print(table1)
print("********************************************************************************")

#Keep ONLY the Duplicates
#intersection_update() ---- keep only the items that are present in both sets.
one={"Green","Blue","Red","Violet"}
two={"Blue",67,True,"Yellow"}           #{"Blue"}
one.intersection_update(two)
print(one)
print("*****************************************************************************")

#intersection()---return a new set, that only contains the items that are present in both sets
number1={100,200,300,400,500}
number2={"Strawberry","Banana","Apple",400}
number3=number1.intersection(number2)
print(number3)                          #{400}
print("*******************************************************************")

#Keep All, But NOT the Duplicates
#symmetric_difference_update() --- keep only the elements that are NOT present in both sets.
task1={"Green","Blue","Red","Violet"}
task2={"Blue",67,True,"Yellow"}           
task1.symmetric_difference_update(task2)
print(task1)
print("**********************************************************")

#symmetric_difference() -- return a new set, that contains only the elements that are NOT present in both sets.
one={"Renu","Beeshma","vismaya"}
two={"Beeshma","Renu",111,564}
three=one.symmetric_difference(two)
print(three)
print("*************************************************************")

#True and 1 are considered the same value in sets, and are treated as duplicates:
value1={100,"rain","sun","cold",True,"wind"}
value2={1,"rain","red","black"}
value3=value1.symmetric_difference(value2)
print(value3)
print("****************************************************************************")



