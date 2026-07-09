'''
Types of Files
a. file with text extension: These files contain plain text and can be opened and edited using text editors. They are commonly used for storing human-readable information, such as documents, code, and configuration files. Examples include .txt, .csv, .log, .md, etc.

b. file with json extension: These files contain data in JavaScript Object Notation (JSON) format, which is a lightweight data interchange format. JSON files are commonly used for storing and exchanging structured data between applications. They can be easily read and written by both humans and machines. Examples include .json files.
Example of a JSON file:
{
    "name": "John Cena",
    "age": 52,
    "city": "Biratnagar"
}

c. file with 

'''

#Changing json to dictionary
import json #json module is used to work with JSON data in Python

personJSON = '{"name": "John Cena", "age": 52, "city": "Biratnagar"}' #JSON string

personDict = json.loads(personJSON) #json.loads() method is used to convert JSON string to Python dictionary
print(personDict) #Printing the dictionary
print(type(personDict)) #Printing the type of the dictionary
print(personDict['name']) #Accessing the value of the key 'name' in the dictionary


#Changing dictionary to json
personDictionary = {
    "name": "John Cena",
    "age": 52,
    "city": "Biratnagar"
}
personJSON = json.dumps(personDictionary) #json.dumps() method is used to convert Python dictionary to JSON string
print(personJSON) #Printing the JSON string
print(type(personJSON)) #Printing the type of the JSON string


#Saving as json file, we can save our data as a JSON file using the json.dump() method. This method takes two arguments: the data to be saved and the file object to which the data will be written. The data can be a Python dictionary, list, or any other serializable object.
personDictionary = {
    "name": "John Cena",
    "age": 52,
    "city": "Biratnagar"
}

with open('./Session_08/files/person.json', 'w') as jsonFile: #with automatically closes the file
    json.dump(personDictionary, jsonFile) #json.dump() method is used to write the dictionary to the JSON file