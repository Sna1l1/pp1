try:
    hours = float(input("Enter hours: "))
except:
    print("Error, please enter numeric input")
    exit(0)
try:
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    exit(0)


above = hours - 40
if above > 0:
    print("Pay:", hours*rate + above*1.5)
else:
    print("Pay:", hours*rate)