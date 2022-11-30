def Quadratic(a, b, c):
    x1 = ((((-b) + (b**2 - 4*a*c)**0.5)/(2*a)))
    x2 = ((((-b) - (b**2 - 4*a*c)**0.5)/(2*a)))
    return x1, x2

a = float(input("Input the co-efficient of x²: "))
b = float(input("Input the co-efficient of x¹: "))
c = float(input("Input the co-efficient of x⁰: "))
ans = Quadratic(a, b, c)
print(ans)