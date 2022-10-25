from random import randint
from xmlrpc.client import MAXINT, MININT


num = randint(MININT, MAXINT)
if num % 2 == 0:
    even = "even"
else:
    even = "odd"

print(f"the number {num} is {even}")
