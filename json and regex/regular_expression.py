#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#RegEX Module
#Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

#RegEx Functions
#Search: Returns a Match object if there is a match anywhere in the string
child1 = "childrens are playing in the park"

test_in_child1 = re.search("^childrens.*park$", child1)

if test_in_child1:
    print("Search Function\nYes! you are right")
    
else:
    print("No..you are wrong...")
    
print("**************************************************************")

#findall:  Returns a list containing all matches

students = "Nithya, Vismaya, Aksha, Mythili are the Computer Science Students.."

stud = re.findall("th", students)

print("Findall\n", stud)

print("***********************************************************")

#split--Returns a list where the string has been split at each match

canteen = "Tea# Coffee&Chocolates#Milk&Horlicks"

at_canteen = re.split("&", canteen)

print("Split\n", at_canteen)

print("***************************************")

#sub	Replaces one or many matches with a string

chaege_name = "My name is pollachi.."

result = re.sub("pollachi","Vismaya", chaege_name)

print("Sub() Function\n", result)

print("******************************************")

#Metacharaters

#[]	A set of characters	"[a-m]"	  (Find all lower case characters alphabetically between "a" and "m":)
task_1 = "India is our Nation"

result_1 = re.findall("[a-m]", task_1)

print("[]	A set of characters	\n", result_1)

print("************************************************************")



#\	Signals a special sequence (can also be used to escape special characters)	"\d"	

task_2 = "My 1st moblile price is 12000"

result_2 = re.findall("\d", task_2)

print("\ Backslash\n", result_2)

print("************************************************************")

#.	Any character (except newline character)	"he..o"	

task_3 = "mobile phones"

result_3 = re.findall("m...l.", task_3)

print(". Any character\n", result_3)

print("************************************************************")

#^	Starts with	"^hello"	

task_4 = "I am from chennai"

result_4 = re.findall("^I", task_4)

print("^Starts with\n", result_4)

print("************************************************************")

#$	Ends with	"planet$"	

task_5 = "my father is an tailor"

result_5 = re.findall("tailor$", task_5)

print("$ Ends with\n", result_5)

print("************************************************************")

#*	Zero or more occurrences	"he.*o"	

task_6 = "We are in office"

result_6 = re.findall("of.*e", task_6)

print("* zero or more occurrences ..\n", result_6)

print("************************************************************")

#+	One or more occurrences	"he.+o"	

task_7 = "Welcome to python"

result_7 = re.findall("py.+n", task_7)

print("+ one or more occurrences \n", result_7)

print("************************************************************")

#?	Zero or one occurrences	"he.?o"	

task_8 = "I am Vismaya"

result_8 = re.findall("Vis.?ya", task_8)

print("? zero or one occurrences \n", result_8)

print("************************************************************")

#{}	Exactly the specified number of occurrences	"he.{2}o"	

task_9 = "He is an Indian"

result_9 = re.findall("In.{3}n", task_9)

print("{} Exactly the specified number of occurrences.. \n", result_9)

print("************************************************************")

#|	Either or	"falls|stays"	

task_10 = "she is playing in the ground"

result_10 = re.findall("ground|home", task_10)

print("| Either or \n", result_10)

if result_10:
    print("Yes!,there is a match...")
    
else:
    print("No Match Found!")

print("************************************************************")

#()	Capture and group	 	 


