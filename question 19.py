x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))
n = 0
if x > y:
    print("The second number has to be GREATER than the first number.")
elif x == y:
    print("The second number has to be GREATER than the first number.")
else:
    for i in range(x, (y+1)):
        n += i
        print(n)