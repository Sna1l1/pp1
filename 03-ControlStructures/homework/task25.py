a = int(input("Enter height: "))
b = int(input("Enter width: "))

s = ""

for i in range(a):
    for j in range(b):
        if i == 0 or i == a-1:
            s += "*"
        else:
            if j == 0 or j == b-1:
                s += "*"
            else:
                s += " "
    s += "\n"
print(s)
        