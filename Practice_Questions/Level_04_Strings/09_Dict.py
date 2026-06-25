
#Create an empty dictionary named dog
dog = {}
print(dog, type(dog))

#Add items to the dog dictionary
dog['name'] = 'Sheru'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

#print the dictionary dog
print(dog)

student = {
    'first_name': 'Karl',
    'last_name': 'Max',
    'gender': 'male',
    'age': 25,
    'married': False,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'Nepal',
    'city': 'Berlin',
}
print(student, len(student))

#get the value of skills and check the data type, it should be a list
print(student['skills'], type(student['skills'])) #It is a list

#Modify the skills values by adding one or two skills
student['skills'].append('C++')
student['skills'].append('Java')
print(student['skills'], type(student['skills'])) #It is a list


#Get the dictionary keys as a list
keys = list(student.keys())
print(keys, type(keys)) #It is a list

#Get the dictionary values as a list
values = list(student.values())
print(values, type(values)) #It is a list

#Get the dictionary items as a list of tuples
items = list(student.items())
print(items, type(items)) #It is a list of tuples


#Delete one of the items in the dictionary
del student['married']
print(student, len(student))

#Delete one of the dictionaries

del student
print(student) #This will raise an error since student has been deleted