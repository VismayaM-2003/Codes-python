#Loop through list
vowels=["a","e","i","o","u"]
for x in vowels:
 print(x)
 
print("****************************************************************")
 
#Loop Through the Index numbers
alphabets=["a","b","c","d","e","f"]
for i in range(len(alphabets)):#Use the range() and len() functions to create a suitable iterable.
    print(alphabets[i])
    
print("****************************************************************")

#while loop
Upper=["A","B","C","D","E"]
i=0
while i<len(Upper):
    print(Upper[i])
    i=i+1

print("****************************************************************")

#Looping using List Comprehension---offers shortest syntax
Apple=["Red","fruit","healthy","juice"]
[print(x) for x in Apple]