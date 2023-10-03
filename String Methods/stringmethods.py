#All string methods return new values. They do not change the original string.
#capitalize()
test="upper case the first letter in this sentence"
a=test.capitalize()
print(a)

print("*******************************************************************************************************")

#casefold()
txt="Lower Case The First Letter In This Sentence"
a=txt.casefold()
print(a)

print("*******************************************************************")

#center()
name="Aksha"
c=name.center(20)
print(c)

print("***********************************************************************************")

#count()	Returns the number of times a specified value occurs in a string
new=" India is the seventh-largest country by area. India is one of the world's most attractive country "
s=new.count("India")
print(s)

print("****************************************************************************************")

#encode()	Returns an encoded version of the string
#syntax=string.encode(encoding=encoding, errors=errors)
Name= "I am Ståle"
val= Name.encode()
print(val)

print("***************************************************************************************")

#endswith()	Returns true if the string ends with the specified value
cls="Welcome to python world."
new_cls=cls.endswith("world.")
print(new_cls)

cls1="Welcome to python world"
new_cls1=cls1.endswith("python world",5,12)
print(new_cls1)

print("****************************************************************************")

#expandtabs()	Sets the tab size of the string
val="H\te\tl\tl\to"
print(val.expandtabs())
print(val.expandtabs(5))
print(val.expandtabs(10))
print(val.expandtabs(15))

print("*************************************************************************************************")

#find()	Searches the string for a specified value and returns the position of where it was found
text="Hello, This is Visual studio here we can learn Python"
a=text.find("a")
print(a)

text1="Hello, This is Visual studio here we can learn Python"
a=text1.find("a",2,5)
print(a)

print("***************************************************************************")

#format()	Formats specified values in a string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

print("*******************************************************************")

#format_map()	Formats specified values in a string

#index()	Searches the string for a specified value and returns the position of where it was found
text="Hello, This is Visual studio here we can learn Python"
a=text.index("a")
print(a)

text1="Hello, This is Visual studio here we can learn Python"
a=text1.find("a",2,5)
print(a)

print("*******************************************************************************************")

#isalnum()	Returns True if all characters in the string are alphanumeric
print("isalnum")
an="Good123Morning"
x=an.isalnum()
print(x)

an1="Good #Morning &"
x=an1.isalnum()
print(x)

print("************************************************************************")

#isalpha()	Returns True if all characters in the string are in the alphabet
print("isalpha")
up="abcde"
x=up.isalpha()
print(x)

up="abede1234"
x=up.isalpha()
print(x)

print("*****************************************************************")

#isascii()	Returns True if all characters in the string are ascii characters
print("isascii")
a="Hello    &#$@"
b=a.isascii()
print(b)

print("**************************************************************************")

#isdecimal()	Returns True if all characters in the string are decimals
print("isdecimal")
numbers="1234"
x=numbers.isdecimal()
print(x)

number1="24 2536 7895 9504"
x=number1.isdecimal()
print(x)

print("******************************************************************")

#isdigit()	Returns True if all characters in the string are digits
print("isdigit")
num1=("ABCD12567")
x=num1.isdigit()
print(x)

num2=("617290")
x=num2.isdigit()
print(x)

print("****************************************************************")

#isidentifier()	Returns True if the string is an identifier
print("isidentifier()")
val1="1Hello"
val2="2_yellow"
val3="my world"
val4="_myWorld"
print(val1.isidentifier())
print(val2.isidentifier())
print(val3.isidentifier())
print(val4.isidentifier())

print("*******************************************************************************")

#islower()	Returns True if all characters in the string are lower case
print("islower()")
num1="Hello World"
num2="good morning 1234"
num3="What are u123 doing?@hdu*&%%$#@"
num4="ThankYou"
print(num1.islower())
print(num2.islower())
print(num3.islower())
print(num4.islower())

print("*********************************************************************")

#isnumeric()	Returns True if all characters in the string are numeric
print("isnumeric()")
a1="1"
a2="-123"
a3="6789"
a4="12.78"
print(a1.isnumeric())
print(a2.isnumeric())
print(a3.isnumeric())
print(a4.isnumeric())

print("******************************************************************")

#isprintable()	Returns True if all characters in the string are printable
print("isprintable()")
txt="Call me later #45?"
print(txt.isprintable())

txt1="Are u \n  busy now?"
print(txt1.isprintable())

print("*******************************************************************")

#isspace()	Returns True if all characters in the string are whitespaces
print("isspace()")
str="    "
print(str.isspace())

str1="     s    v    n"
print(str1.isspace())

print("*******************************************************")

#istitle()	Returns True if the string follows the rules of a title
#True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
#Symbols and numbers are ignored
print("istitle()")
head="Today News Headlines"
print(head.istitle())

head1="Today news heaslines"
print(head1.istitle())

print("**********************************************")

#isupper()	Returns True if all characters in the string are upper case
print("isupper()")
txt1="my world is full of music"
txt="MY DEAR TEDDY"
print(txt1.isupper())
print(txt.isupper())

print("***************************************************")

#join()	Converts the elements of an iterable into a string
print("join()")
group=("Python","is","a","popular","programming","language")
x="#".join(group)
print(x)

print("*****************************************************")

#ljust()	Returns a left justified version of the string
fav_1="apple"
x=fav_1.ljust(30)
print(x,"is good for health")

fav="Apple"
x=fav.ljust(30,"O")
print(x)

print("****************************************")

#lower()	Converts a string into lower case
number="HELLO My dear FrIENDS"
print(number.lower())

print("***************************************************************")

#lstrip()	Returns a left trim version of the string
#removes any leading characters (space is the default leading character to remove)
str="       Student       "
x=str.lstrip()
print(x)

str1="He is my Student ,Very good boy"
x=str1.lstrip("He is my ")
print(x)

print("**************************************************************************")

#maketrans()	Returns a translation table to be used in translations
txt="Can you call me later?"
x="amltyue"
y="enmuxvt"
mytable=str.maketrans(x,y)
print(txt.translate(mytable))

print("*************************************************************")

#partition()	Returns a tuple where the string is parted into three parts
text="python was created in the year of 1991"
x=text.partition("created")
print(x)

print("************************************************************************")

#replace()	Returns a string where a specified value is replaced with a specified value
sample="she is from India"
x=sample.replace("India","Jappan")
print(x)

print("************************************************************************************")

#rfind()	Searches a specified value ,returns the last position of where it was found,method finds the
#last occurrence of the specified value, returns -1 if the value is not found,almost same as rindex()
example="Hi I am Kishore"
x=example.rfind("Kishore")
print(x)

print("***************************************************************************************")

#rindex()	Searches the string for a specified value and returns the last position of where it was found
"""Traceback (most recent call last):
  File "demo_ref_string_rfind_vs_rindex.py", line 4 in <module>
    print(txt.rindex("q"))
ValueError: substring not found"""

#rjust()	Returns a right justified version of the string
fav_1="apple"
x=fav_1.rjust(30)
print("I Love",x)

fav="Apple"
x=fav.rjust(30,"O")
print(x)

print("****************************************************************")

#rpartition()	Returns a tuple where the string is parted into three parts
text="I have listen Music every day ,Music is best medicine for everything !"
x=text.rpartition("Music")
print(x)

text="I have listen Music every day ,Music is best medicine for everything !"
x=text.rpartition("Apples")
print(x)

print("*****************************************************************************")

#rsplit()	Splits the string at the specified separator, and returns a list
#Split a string into a list, using comma, followed by a space (, ) as the separator
table="Mouse,Keyboard,Monitor"
x=table.rsplit(", ")
print(x)
# setting the maxsplit parameter to 1, will return a list with 2 elements!
table="Mouse, Keyboard, Monitor"
x=table.rsplit(", ", 1)
print(x)

print("***********************************************************************")

#rstrip()	Returns a right trim version of the string
str="       Student       "
x=str.rstrip()
print(x)

str1="He is my Student ,Very good boy"
x=str1.rstrip(",Very good boy")
print(x)

#split()	Splits the string at the specified separator, and returns a list
#splits a string into a list.You can specify the separator, default separator is any whitespace.
ex1="Hello, My Name is Vismaya, I am 5 years old"
x1=ex1.split(", ")
print(x1)

ex2="python#is#a#easiest#language"
x2=ex2.split("#")
print(x2)

ex3="hello welcome python"
x3=ex3.split(" ", 2)
print(x3)

print("***************************************************************")

#splitlines()	Splits the string at line breaks and returns a list
line1="Welcome to home\n, Thankyou for coming and glad to meet you"
x1=line1.splitlines()
print(x1)

line2="Welcome to home\n, Thankyou for coming and glad to meet you"
x2=line2.splitlines(True)
print(x2)

print("*******************************************************************")

#startswith()	Returns true if the string starts with the specified value
text1="Python is used to create web applications"
x1=text1.startswith("web")
print(x1)

text2="Python is used to create web applications"
x2=text2.startswith("used",10,14)
print(x2)

print("****************************************************************")

#strip()	Returns a trimmed version of the string
task1="        Python       "
x1=task1.strip()
print(x1)

task2="Welcome to Python ,Python is used to create web applications"
x2=task2.strip("Welcome to Python,")
print(x2)

print("**********************************************************************************************")

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
Ex1="Pyton TUtorial Is vERY USEful FOr deVElopERS"
x=Ex1.swapcase()
print(x)

print("***********************************************************")

#title()	Converts the first character of each word to upper case
head1="today news headlines"
x1=head1.title()
print(x1)

head2="india got freedom in 1947 15th august"
x2=head2.title()
print(x2)

print("**********************************************")

#translate()	Returns a translated string
txt="Can you call me later?"
x="amltyue"
y="enmuxvt"
mytable=str.maketrans(x,y)
print(txt.translate(mytable))

print("***************************************************************************")

#upper()	Converts a string into upper case
txt="Can you call me later"
x=txt.upper()
print(x)

print("*********************************************************************************************")

#zfill()	Fills the string with a specified number of 0 values at the beginning
#Fill the string with zeros until it is no of characters long
number="78"
x=number.zfill(30)
print(x)
