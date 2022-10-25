amount = int(input("Enter the amount in PLN: "))

c5 = 0
c2 = 0
c1 = 0

while c5 < amount:
    c5 += 1
    amount -= 5
while c2 < amount:
    c2 += 1
    amount -= 2
while c1 < amount:
    c1 += 1
    amount -= 1

print(f"5 zl - {c5}")
print(f"2 zl - {c2}")
print(f"1 zl - {c1}")