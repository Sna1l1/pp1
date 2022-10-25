from random import randint


dice = randint(1, 6)

guess = int(input("Write a number from 1 to 6: "))

print(dice == guess)