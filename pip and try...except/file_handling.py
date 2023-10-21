#1.Python File Handling
#Python has several functions for creating, reading, updating, and deleting files.

#open() function--The key function for working with files in Python.
#It two parameters; filename, and mode(method).

#Methods for opening a file.
# "r" - Read
# "a" - Append
# "w" - Write
# "x" - Create

#specify, if the file should be handled as binary or text mode
# "t" - Text
# "b" - Binary

#Syntax

#file = open("C:\python\Doubts.txt")

#file = open("C:\python\Doubts.txt", "rt")

#"r" for read, and "t" for text are the default values, you do not need to specify them.


#2.Python Read Files
#read() method for reading the content of the file:

file = open("Newfile.txt", "r")

print(file.read())     #read the content of the file.

print("**********************************************************")

#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

print("Return the 20 first characters of the file:")

file = open("Newfile.txt", "r")

print(file.read(20))   

print("*******************************************************")

#Read Lines
print("Read one line of the file:")

file = open("Newfile.txt", "r")

print(file.readline())

print("*************************************")

#Read two lines of the file:
print("Read first 2 line")

file = open("Newfile.txt", "r")

print(file.readline())

print(file.readline())

print("*******************************************************")

#Loop through the file line by line:

print("for loop")

file = open("Newfile.txt", "r")

for i in file:
    print(i)
    
print("*****************************")

#Close Files
file = open("Newfile.txt", "r")

print(file.readline())

file.close()

print("**********************")

#3.Python Write/Create Files

#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

#"a"
file = open("Newfile.txt", "a")

file.write("This is the Poem")

file.close()

file = open("Newfile.txt", "r")

print("Append \n", file.read())

print("*****************************************")

#"w"
file = open("Newfile.txt", "w")

file.write("There is nothing....")

file.close()

file = open("Newfile.txt", "r")

print("Overwrite \n", file.read())

print("**********************************************")

#Create a New File

#"x" - Create - will create a file, returns an error if the file exist

#"a" - Append - will create a file if the specified file does not exist

#"w" - Write - will create a file if the specified file does not exist

file = open("NEW.txt", "x")

file = open("NEW.txt", "w")

print("**********************")


