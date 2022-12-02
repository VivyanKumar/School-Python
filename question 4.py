def Quadratic(a, b, c):
    x1 = ((((-b) + (b**2 - 4*a*c)**0.5)/(2*a)))
    x2 = ((((-b) - (b**2 - 4*a*c)**0.5)/(2*a)))
    return x1, x2
x = float(input("Input the co-efficient of x²: "))
y = float(input("Input the co-efficient of x¹: "))
z = float(input("Input the co-efficient of x⁰: "))
print(Quadratic(x, y, z))