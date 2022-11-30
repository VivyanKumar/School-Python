x = int(input("Input the start of the range: "))
y = int(input("Input the end of the range: "))
a = int(input("Input the number to be tested: "))
if a in range(x, y):
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
else:
    print('The number is not in the range.')