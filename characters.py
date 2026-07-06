import random as r

@staticmethod
def password_generator():
    #the raw data
    lowercase_alphabets = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_alphabets = list("abcdefghijklmnopqrstuvwxyz".upper())
    numbers = list("1234567890")
    symbols = list("!@#$%^&*+?~")

    characters = lowercase_alphabets + numbers + symbols + uppercase_alphabets

    #gets a random size from 8-16 characters
    size = r.randint(8, 16)
    
    #a blank list
    password_as_list = []

    #appends each character in the list for creating password
    for i in range(size):
        password_as_list.append(r.choice(characters))

    #converts the list into string
    password = "".join(password_as_list)

    return password
