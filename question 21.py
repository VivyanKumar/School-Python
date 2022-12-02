import re
print("The accepted values for hex are: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)")
h = str(input("Input the value in hex: "))
hexa = "0x" + h
while True:
    if (bool(re.match('^[0123456789ABCDEFabcdef]+$', h))) != True:
        print("Invalid input.")
        print("The accepted values for hex are: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)")
    else:
        print(int(hexa, 16))
        break