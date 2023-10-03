#Access Tuple items---- by referring to the index number, inside square brackets
one=("Sunday","Monday","Tuesday","Wednesday","Thursday")
print(one[4])   #Thursday
print("**********************************************************************")

#Negative indexing---print items from the end
two=("Saturady","Friday","Thursday","Wednesday","Monday")
print(two[-1])   #Monday
print("***********************************************************************************")

#Range of Indexes
three=("Tom","Jerry","Duck","Peacock","Rabbit")
print(three[1:5])     #("Jerry","Duck","Peacock","Rabbit")
print(three[:4])      #("Tom","Jerry","Duck","Peacock")
print(three[2:])      #("Duck","Peacock","Rabbit")
print("*********************************************************************************")

#Range of Negative Indexes
four=("Tennis","Cricket","Football","Chess","Carrom")
print(four[-4:-1])      #("Cricket","Football","Chess")
print("***********************************************************************************")

#Check if Item Exists
five=("Cat","Tiger","Lion","Dog","Cow")
if "Cat" in five:
    print("Yes,'Cat' in five")#"Yes,'Cat' in five"
    
six=("Cat","Tiger","Lion","Dog","Cow")
if "Parrot" in six:
    print("Yes,'Parrot' in six")
else:
    print("No,'Parrot' not in six")#No,'Parrot' not in six
print("******************************************************************")    


    