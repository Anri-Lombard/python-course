# In C++ and Java Docstrings come in before the function declaration.
# In Python the come inside the function definition.
# Hereby they become an attribute of a function.
# This is because everything in Python is an object and has an attribute.

import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user, until
    a valid `int` is entered.

    :param prompt: The String that the user will see, when they're
        prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print(f"{temp} is not a valid number")


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
