from audioop import avg, avgpp
from itertools import count
from operator import countOf
from statistics import mean


numbers = []

while True: 
    try:
        inp = input("Enter a number: ")
        if inp == "done":
            print("total:", sum(numbers))
            print("count:", numbers.__len__())
            print("average:", mean(numbers))
            exit(0)
        elif inp == "exit":
            exit(0)
        numbers.append(int(inp))
    except:
        print("Invalid input")
        exit(0)
        