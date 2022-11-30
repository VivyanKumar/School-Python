pi = 3.141592653589793
def shape():
    Shape = str(input("What shape do you want? Circle, Triangle, Square, Rectangle (C/T/S/R) "))
    return Shape
def AorP():
    AorP = str(input("What do you want to calculate? Area or Perimeter (A/P) "))
    return AorP
def circle(r):
    CA = pi * r * r
    return CA
def CirclePeri (r):
    CP = pi * 0.5 * r
    return CP
def heron(a, b, c):
    s = ((a + b + c)/2)
    TA = ((s(s-a)*(s-b)*(s-c))**0.5)
    return TA
def TrianglePeri(a, b, c):
    TP = a + b + c
    return TP
def Square(s):
    SA = s ** 2
    return SA
def SquarePeri(s):
    SP = 4 * s
    return SP
def Rectangle(l, b):
    RA = l * b
    return RA
def RectanglePeri(l, b):
    RP = ((l + b) * 2)
    return RP

while True:
    ans = shape()
    ans2 = AorP()

    if ans == "C" and ans2 == "A":
        r = float(input("Type the value of the radius: "))
        print(circle(r))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "C" and ans2 == "P":
        r = float(input("Type the value of the radius: "))
        print(CirclePeri(r))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "T" and ans2 == "A":
        a, b, c = map(float,input("Input the values in the format 'A B C' ").split())
        print(heron(a, b, c))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "T" and ans2 == "P":
        a, b, c = map(float,input("Input the values in the format 'A B C' ").split())
        print(TrianglePeri(a, b, c))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "S" and ans2 == "A":
        s = float(input("Type the value of the side: "))
        print(Square(s))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "S" and ans2 == "P":
        s = float(input("Type the value of the side: "))
        print(SquarePeri(s))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "R" and ans2 == "A":
        l, b = map(float,input("Input the values of length and breath in the format 'L B' ").split())
        print(Rectangle(l, b))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue
    elif ans == "R" and ans2 == "P":
        l, b = map(float,input("Input the values of length and breadth in the format 'L B' ").split())
        print(RectanglePeri(l, b))
        x = input("Do you wish to calculate again?: (Y/N)")
        if x == 'N':
            print("Okay, Thanks for using my program!")
            break
        elif x == 'Y':
            continue
        else:
            print("Invalid Input")
            continue