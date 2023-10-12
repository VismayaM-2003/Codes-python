#Iterators--an object that contains a countable number of values,meaning that you can traverse through all the values.
#Methods __iter__() and __next__().

#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects

#iter()--which is used to get an iterator
#Return an iterator from a tuple, and print each value:

fruits = ("Jackfruit","Watermelon","Strawberry")
result = iter(fruits)

print(next(result))
print(next(result))
print(next(result))

print("*******************************************")

#Strings are also iterable objects, containing a sequence of characters:

name = "VismayaMurugan"
i = iter(name)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print("**********************************************")

#Looping Through an Iterator--for loop

colors = ("blue","Orange","violet")
for i in colors:
    print(i)
    
print("**************************************")

#Iterate the characters of a string using for loop
greet = ("Welcome")
for x in greet:
    print(x)
    
print("*****************************************")

#Create an Iterator
#create an object/class as an iterator we have to implement the methods __iter__() and __next__() to your object.
#The __iter__()-acts similar ,do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() -also allows do operations, and must return the next item in the sequence.
class numbers:
    def __iter__(self):
        self.x = 10
        return self
    
    def __next__(self):
        a = self.x
        self.x += 1
        return a
mycls = numbers()
i = iter(mycls)

print(next(i))
print(next(i))
print(next(i))

print("*********************************************************")

#Stopiteration
#In the __next__() method, we can add a terminating condition to raise an error 
#if the iteration is done a specified number of times
class stud:
    def __iter__(self):
        self.a = 11
        return self
    
    def __next__(self):
      if self.a <= 15:
        x = self.a
        self.a += 1
        return x
      else:
        raise StopIteration
    
myhome = stud()
i = iter(myhome)

for x in i:
    print(x)
    
print("**********************************")

    

    
    