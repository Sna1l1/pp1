s = ""
for i in range(1, 6):
    for _ in range(i):
        s += "* "
    s += "\n"
for i in range(4, 0, -1):
    for _ in range(i):
        s += "* "
    s += "\n"
print(s)