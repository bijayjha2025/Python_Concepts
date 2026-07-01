# Write a function which generates a six digit/character random_user_id.

def generateRandomUserId():
    import random
    import string

    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(6))
    return random_id

userId = generateRandomUserId()
print(f"Generated random user ID: {userId}")


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def userIdByGenByUser():
    import random
    import string

    numChars = int(input("Enter the number of characters for the user ID: "))
    numIds = int(input("Enter the number of user IDs to generate: "))

    characters = string.ascii_letters + string.digits
    userIds = [''.join(random.choice(characters) for _ in range(numChars)) for _ in range(numIds)]
    return userIds

userIds = userIdByGenByUser()
print(f"Generated user IDs: {userIds}")
