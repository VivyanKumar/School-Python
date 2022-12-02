pi = 3.142
def heron(a,b,c):
    s = (a + b + c)/2
    ar = (s(s-a)(s-b)(s-c))**0.5
    return ar
shape = input("Circle, Triangle, Square or Rectangle? (C/T/S/R)")
if shape == 'C' or 'c':
    r = float(input("What is the radius? "))
    print("Perimeter:", (2 * pi * r), "Area:", (pi * r * r))
elif shape == 'T' or 't':
    x, y, z = map(float,input("Please enter the 3 sides (Format: 9 7 2) "))
    print("Perimeter:", sum(x, y, z), "Area:", heron(x, y, z))
elif shape == 'S' or 's':
    s = float(input("What is the length of the side? ").split())
    print("Perimeter:", (4 * s), "Area:", (s ** 2))
elif shape == 'R' or 'r':
    l, b = map(float,input("What is the length and breadth? (Format: 12 4) ").split())
    print("Perimeter:", (2 * (l + b)), "Area:", (l * b))
else:
    print("Invalid Input.")