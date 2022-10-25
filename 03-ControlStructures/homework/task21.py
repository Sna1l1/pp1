university = "UEK w Krakowie"
s = ""
for char in list(university):
    s += char.replace(char, char + " ")
print(s)