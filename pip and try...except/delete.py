#Python Delete Files
#To delete a file, you must import the OS module, and run its os.remove() function:
import os
#os.remove("NEW.txt")

#Check if File exist:
"""if os.path.exists("NEW.txt"):
  os.remove("NEW.txt")
else:
  print("The file does not exist")"""
  
print("***************************************************")

#Delete a folder
#os.rmdir() method:

#os.rmdir("Vichu")

if os.path.exists("Vichu"):
  os.remove("Vichu")
else:
  print("The folder does not exist")

