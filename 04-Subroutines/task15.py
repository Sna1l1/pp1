from 0
from 04-Subroutines.mymath import read_number4-Subroutines.mymath import generate_number
import mymath

while True:
    num = mymath.read_number()
    rand = mymath.generate_number()
    if num == rand:
        print("You won!")
        pass
    else:
        print("Numbers are different")