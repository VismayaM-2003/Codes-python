#Python Loops
# Python has two primitive loop commands:
# while loops and for loops

#while Loop-- we can execute a set of statements as long as a condition is true.
a = 11
while a < 16:
  print(a)
  a += 1
print("*********************************************")

#break Statement-- we can stop the loop even if the while condition is true
i = 20
while i < 30:
  print(i)
  if (i == 22):
    break
  i += 1
print("*********************************************************")

#continue Statement-- we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("******************************************************************")

#else Statement--we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  
