import random
from tkinter import *
import doctest

""""
This function generates a random password.

    Parameters:
        length (int): The length of the password.
        chars (boolean): If true, the password will contain characters.
        ints (boolean): If true, the password will contain numbers.
        specials (boolean): If true, the password will contain special characters.
        Returns:
            password (string): The generated password.
>>> generate_password(8, True, True, True)

"""
def generate_password(length, chars, ints, specials):
    if (not (chars or ints or specials)):
        return "Invalid input"
    password = ""
    possible_choices = ""
    if chars:
        possible_choices += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if ints:
        possible_choices += "0123456789"
    if specials:
        possible_choices += "!@#$%^&*()_+"
    for i in range(length):
        password += random.choice(possible_choices)
    return password



if __name__ == "__main__":
    create_gui()


