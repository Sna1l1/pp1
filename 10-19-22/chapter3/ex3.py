try:
    score = float(input("Enter score: ")) 
except:
    print("Bad score")
    exit(0)

if score >= .9: 
    print("A")
elif score >= .8:
    print("B")
elif score >= .7:
    print("C")
elif score >= .6:
    print("D")
elif score < .6:
    print("F")