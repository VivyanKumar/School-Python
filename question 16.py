f = 1
n = int(input("Enter an integer here: "))
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is one")
else:
    for i in range(1, n + 1):
        f = f * i
    print("The factorial of", n, "is", f)