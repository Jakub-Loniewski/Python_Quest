import random
import string

characters = list(string.ascii_letters + string.digits + "[email protected]#$%^&*()")

def random_password():

    length = int(input("Enter password length: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))
random_password()
