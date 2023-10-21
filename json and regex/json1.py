
#JavaScript Object Notation (JSON)
#It is a standardized format commonly used to transfer data as text that can be sent over a network.
#It's used by lots of APIs and Databases, and it's easy for both humans and machines to read. 
#JSON represents objects as name/value pairs, just like a Python dictionary.
#Python has a built-in package called json, which can be used to work with JSON data.
import json

#Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method.

details  = '{ "name":"Vismaya", "gender":"female", "education":"B.Sc.Computer Science" }'

new_details = json.loads(details)  #parse details

#the result will be python dictionary
print("Student gender is : ",new_details["gender"])

print("*********************************************************")


#convert from python to json
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

details = {
    "name": "Vismaya",
    "gender": "Female",
    "education": "B.Sc.Computer Science"           
}

new_details = json.dumps(details)

print("The details of the student....\n",new_details)

print("****************************************")

#Convert Python objects into JSON strings, and print the values:

print("Dictionary: ",json.dumps({"Language": "python", "year": 2023}))
print("List: ",json.dumps(["c", "c++"]))
print("Tuples: ",json.dumps(("Vismaya", "Murugan")))
print("String: ",json.dumps("Welcome To The python world..."))
print("Integer: ",json.dumps(42))
print("Float: ",json.dumps(31.76))
print("True in Boolean: ",json.dumps(True))
print("False in boolean: ",json.dumps(False))
print("None--",json.dumps(None))

print("**************************************************************")

#Convert a Python object containing all the legal data types:
candidate = {
    "name": "Vismaya",
    "Skills":
        {"Languages": "PYTHON,HTML,CSS,JAVASCRIPT"},
    "Married": False,
    "Female": True, 
    "Children": None,
    "Year of passed out": 2023,
    "prefered Locations": ("Bangalore", "Chennai", "Coimbatore"),
    "Location": "pollachi-coimbatore",
    "State": "Tamilnadu",
    "Institution": "Government Arts College Udumalpet.."
}

print("Convert a Python object containing all the legal data types..\n",json.dumps(candidate))

print("****************************************************************")

#Format the result
#The json.dumps() method has parameters to make it easier to read the result:

candidate = {
    "name": "Vismaya",
    "Skills":
        {"Languages": "PYTHON,HTML,CSS,JAVASCRIPT"},
    "Married": False,
    "Female": True, 
    "Children": None,
    "Year of passed out": 2023,
    "prefered Locations": ("Bangalore", "Chennai", "Coimbatore"),
    "Location": "pollachi-coimbatore",
    "State": "Tamilnadu",
    "Institution": "Government Arts College Udumalpet.."
}

print("Format the result with indentation...\n",json.dumps(candidate,indent=5,separators=(". ", " = ")))

print("**************************************************************")

#Order the Result
#Use the sort_keys parameter to specify if the result should be sorted or not:

candidate = {
    
    "name": "Vismaya",
    
    "Skills":
        {"Languages": "PYTHON,HTML,CSS,JAVASCRIPT"},
        
    "Married": False,
    
    "Female": True, 
    
    "Children": None,
    
    "Year of passed out": 2023,
    
    "prefered Locations": ("Bangalore", "Chennai", "Coimbatore"),
    
    "Location": "pollachi-coimbatore",
    
    "State": "Tamilnadu",
    
    "Institution": "Government Arts College Udumalpet.."
    
}

print("Sort the Details...\n",json.dumps(candidate,indent=5,sort_keys=True))

