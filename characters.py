import random as r

@staticmethod
def password_generator():
    lowercase_alphabets = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_alphabets = list("abcdefghijklmnopqrstuvwxyz".upper())
    numbers = list("1234567890")
    symbols = list("!@#$%^&*+?~")

    characters = lowercase_alphabets + numbers + symbols + uppercase_alphabets

    size = r.randint(8, 16)

    password_as_list = []

    for i in range(size):
        password_as_list.append(r.choice(characters))

    password = "".join(password_as_list)

    return password