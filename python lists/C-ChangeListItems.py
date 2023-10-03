#Change item value----specify the  index number
Devices=["Keyboard","Mouse","Monitor","CPU","Scanner"]
Devices[3]="Computer"
print(Devices)

print("*****************************************")

#change a range of item values
Names=["Vismaya","Prabha","Sri","Janu","Lavi","Abi","Malar"]
Names[1:5]="Pavi","Jerlin","Sumi","Sandy"
print(Names)

print("******************************************************************")

#change a second value by 2values
Rainbow=["Violet","indico","Blue"]
Rainbow[1:2]="Green","Yellow"
print(Rainbow)

print("********************************************************************************")

#insert items
Numbers=["1","2","3","4","5","6"]
Numbers.insert(3,1000)
print(Numbers)