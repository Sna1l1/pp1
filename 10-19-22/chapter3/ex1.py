hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

above = hours - 40
if above > 0:
    print("Pay:", hours*rate + above*1.5)
else:
    print("Pay:", hours*rate)