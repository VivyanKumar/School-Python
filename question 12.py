a = float(input("Input first number to be compared: "))
b = float(input("Input second number to be compared: "))
c = float(input("Input third number to be compared: "))
if a > b and a > c:
    print(a, "is the largest number out of the three")
elif b > a and b > c:
    print(b, "is the largest number out of the three")
elif c > a and c > b:
    print(c, "is the largest number out of the three")
elif a == b == c:
    print("They are all equal, so there is no largest number!")
else:
    print("Invalid Input")