i = 0
while(i < 3):
    code = input("Enter the PIN code: ")
    if code != "0805":
        print("Incorrect...")
        i += 1
    else:
        print("Correct!")
        exit(0)
print("Sorry, your payment card has been blocked.")