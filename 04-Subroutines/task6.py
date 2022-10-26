def display_numbers():
    s = ""
    for i in range(1,10):
        if i % 3 == 0:
            s += str(i) + "\n"
        else:
            s += str(i) + " "
    print(s)

display_numbers()