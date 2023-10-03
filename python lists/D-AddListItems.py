#Append Items
Friends=["Viji","Anu","Swetha","Vismaya","Malar"]
Friends.append("Archana")
print(Friends)

print("*********************************************************************")

#insert items
String=["1234","Hello","Python","World"]
String.insert(1,"Vismaya")
print(String)

print("***********************************************************")

#Extend List---To append another list to the current list
Friends=["Viji","Anu","Swetha","Vismaya","Malar"]
String=["1234","Hello","Python","World"]
String.extend(Friends)
print(String)

print("***********************************************************")

#using extend add any iterable like tuples,set
List=["100","200","300","400"]
Tuple=("500","600","700","800")
List.extend(Tuple)
print(List)
