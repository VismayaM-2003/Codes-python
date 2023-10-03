#1.Lists are used to store multiple item in one variable [1.ordered 2.changeable 3.Allow Duplicates]
List=["C","C++","Python"]
print(List)

#ordered
print(List.append("Java"))#if we add a new item to list it will add at the end.
print(List)

print("----------------------------------------------------------------------------------------")

#changeable
List[0]="Hello"    #change
print(List)

print(List.remove("C++"))#remove or add
print(List)

print("----------------------------------------------------------------------------------------")

#Allow Duplicates
List=["Java","Python","HTML","CSS","HTML","Python"]
print(List)

print("***************************************************************************************************")

#2.List Length
print(len(List))#Length of the list

print("************************************************************************************")

#3.List Itmes-Data Types
    #can be of any data type 
Listitems1=["100","200","400","900"]#int
Listitems2=["Vismaya","1234","pink","Hello"]#string
Listitems3=["True","False","True"]#boolean
print(Listitems1)
print(Listitems2)
print(Listitems3)

#list  can contain different data types
List=["56","Hello","899","True","12.90"]
print(List)

print("****************************************************")

#Type()
print(type(Listitems2))

print("****************************************************")

#list()constructor
languages=list(("Tamil","English","Maths"))#double rounded brackets
print(languages)

print("***********************************************")

"""Python Collections(Arrays)
List        :ordered,Changeable,Allow duplicate members.
Tuple       :ordered,unChangeable,Allow duplicate members.
Set         :unordered,unChangeable(remove,add items),unindexed,No duplicate members.
Dictionary  :ordered(version 3.7),unordered(version 3.6 and earlier)Changeable,No duplicate members.

"""







