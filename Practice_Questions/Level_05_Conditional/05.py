
details = {
    'first_Name': 'Elon',
    'last_Name': 'Musk',
    'age': 50,
    'county': 'Nepal',
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'address':{
        'street': 'This Street',
        'zipcode': '12345'
    }
}

#check if the details has skills key, print the middle skill in the skills list.
if 'skills' in details:
    middleSkillsIndex = len(details['skills']) // 2
    print(f"The middle skill is: {details['skills'][middleSkillsIndex]}")

#Check if the skills key has Python or not
if 'skills' in details and 'Python' in details['skills']:
    print("Python is present in the skills list.")

else:
    print("Python is not present in the skills list.")


#Check if it has only Javascript and React as skills and if yes print 'he is front end developer', if only Python is present in skills print 'he is a backend developer', if both Python and Javascript are present, print 'he is a full stack developer', else print 'unknown title'

if 'skills' in details:
    skills = details['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer.")
    elif 'Python' in skills and len(skills) == 1:
        print("He is a backend developer.")
    elif 'Python' in skills and 'JavaScript' in skills:
        print("He is a full stack developer.")
    else:
        print("Unknown title.")


# Check if the person is married or not, print 'he is married' if True, else print 'he is not married'
if 'is_married' in details:
    if details['is_married']:
        print("He is married.")
    else:
        print("He is not married.")

#Check if the person lives in Nepal, print 'he lives in Nepal' if True, else print 'he does not live in Nepal'
if 'county' in details:
    if details['county'] == 'Nepal':
        print("He lives in Nepal.")
    else:
        print("He does not live in Nepal.")
    