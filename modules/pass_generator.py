import string
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += choice(numbers)

    for i in range(4):
        shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password
