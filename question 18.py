num = int(input("Input the positive integer to be checked here: "))
l = len(str(num))
digit = [int(d) for d in str(num)]
arm = [i ** l for i in digit]
s = sum(arm[0:])
if s == num:
    print(num, "is an armstrong number.")
else:
    print(num, "is not an armstrong number.")