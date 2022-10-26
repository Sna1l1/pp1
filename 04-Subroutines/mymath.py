from random import randint


def read_number():
    i = int(input("Enter a number"))
    return i

def generate_number():
    return randint(1, 9)