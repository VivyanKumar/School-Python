
while True:
    x = input("What would you like to do? Add, Subtract, Multiply, Divide, or Exponent? (A,S,M,D,E) ")
    a = float(input("Input the first number: "))
    b = float(input("Input the second number: "))
    if x == 'A':
        print("The sum of", a, "and", b, "is", (a + b))
    elif x == 'S':
        print("The subtraction of", a, "and", b, "is", (a - b))
    elif x == 'M':
        print("The product of", a, "and", b, "is", (a * b))
    elif x == "D":
        print("The division of", a, "and", b, "is", (a / b))
    elif x == "E":
        print("The Exponent of", a, "to the power of", b, "is", (a ** b))
    else:
        print("Invalid input")
    y = input("Do you wish to do another calculation? (Y/N)")
    if y == 'Y' or 'y':
        print("Okay!")
        continue
    elif y == 'N' or 'n':
        print("Okay! Thank you for using my calculator!")
        break
    else:
        print("Invalid input")