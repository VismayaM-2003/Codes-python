#Nested Dictionary
#A dictionary can contain dictionaries, this is called nested dictionaries.
College={
    "First_year":{
        "strength":100,
        "year":"2020-2021"
         },
    "Second_year":{
        "strength":50,
        "year":"2021-2022"
         },
    "Third_year":{
        "strength":70,
        "year":"2022-2023"
         }
}
print(College)
print("***************************************************************")

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries
First_year={
        "strength":100,
        "year":"2020-2021"
         }
Second_year={
        "strength":50,
        "year":"2021-2022"
         }
Third_year={
        "strength":70,
        "year":"2022-2023"
    }
College={
    "First_year": First_year,
    "Second_year": Second_year,
    "Third_year": Third_year
}
print(College)
print("*************************************************************************")

#Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, 
#starting with the outer dictionary
College={
    "First_year":{
        "strength":100,
        "year":"2020-2021"
         },
    "Second_year":{
        "strength":50,
        "year":"2021-2022"
         },
    "Third_year":{
        "strength":70,
        "year":"2022-2023"
         }
}
print(College["Third_year"]["strength"])

