#Update Tuples-Tuples are unchangeable,that cannot change,add,or remove items once the tuple is created.
#But there are some workarounds.

#Change Tuple Values
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
Task1=("Red","Green","Blue")
Task2=list(Task1)
Task2[1]="Violet"
Task1=tuple(Task2)
print(Task1)
print("*********************************************************")

#Add Items
one=(1,2,3,4,5,6,7)#convert into list
two=list(one)
two.append(8)
one=tuple(two)
print(one)

three=("Welcome","to","Hello")#Add tuple to a tuple using +=
four=("World",)
three+=four
print(three)
print("***********************************************")

#Remove Items
five=("Light","Switch","Fan","Tv","Radio")
six=list(five)
six.remove("Light")
five=tuple(six)
print(five)

"""numbers=(1,2,3,5,78,0,5,6)
del numbers
print(numbers)
Traceback (most recent call last):
  File "c:\Users\ELCOT\Pictures\Desktop\Vichu\Tuples\Update_tubles.py", line 35, in <module>
    print(numbers)
          ^^^^^^^
NameError: name 'numbers' is not defined"""
print("******************************************************************")



