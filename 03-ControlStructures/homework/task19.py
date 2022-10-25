dog = int(input("Enter the dog's age in human years: "))
hum = 0

for i in range(dog):
    if i == 0 or i == 1:
        hum += 10.5
    else:
        hum += 4
print(f"The dog's age in dog’s years is {hum} years.")