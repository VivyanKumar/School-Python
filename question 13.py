def add(a, b):
    sum = a + b
    return sum
def sub(a, b):
    sub = a - b
    return sub
def prod(a, b):
    prod = a * b
    return prod
def divi(a, b):
    divi = a / b
    return divi
def power(a, b):
    power = a ** b
    return power

while True:
    x = input("What would you like to do? Add, Subtract, Multiply, Divide, or Exponent? (A,S,M,D,E) ")
    a = float(input("Input the first number: "))
    b = float(input("Input the second number: "))
    if x == 'A':
        print("The sum of", a, "and", b, "is", add(a, b))
        y = input("Do you wish to do another calculation? (Y/N)")
        if y == 'Y':
            print("Okay!")
            continue
        elif y == 'N':
            print("Okay! Thank you for using my calculator!")
            break
        else:
            print("Invalid input")
    elif x == 'S':
        print("The subtraction of", a, "and", b, "is", sub(a, b))
        y = input("Do you wish to do another calculation? (Y/N)")
        if y == 'Y':
            print("Okay!")
            continue
        elif y == 'N':
            print("Okay! Thank you for using my calculator!")
            break
        else:
            print("Invalid input")
    elif x == 'M':
        print("The product of", a, "and", b, "is", prod(a, b))
        y = input("Do you wish to do another calculation? (Y/N)")
        if y == 'Y':
            print("Okay!")
            continue
        elif y == 'N':
            print("Okay! Thank you for using my calculator!")
            break
        else:
            print("Invalid input")
    elif x == "D":
        print("The division of", a, "and", b, "is", divi(a, b))
        y = input("Do you wish to do another calculation? (Y/N)")
        if y == 'Y':
            print("Okay!")
            continue
        elif y == 'N':
            print("Okay! Thank you for using my calculator!")
            break
        else:
            print("Invalid input")
    elif x == "E":
        print("The Exponent of", a, "to the power of", b, "is", power(a,b))
        y = input("Do you wish to do another calculation? (Y/N)")
        if y == 'Y':
            print("Okay!")
            continue
        elif y == 'N':
            print("Okay! Thank you for using my calculator!")
            break
        else:
            print("Invalid input")
    else:
        print("Invalid input")
