num = int(input("Input number to be checked here: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
        else:
            continue

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")