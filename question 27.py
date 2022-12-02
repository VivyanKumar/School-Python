num = float(input("Enter the number you want to round off here: "))
if int(num) == num:
    print(num, "is already a whole number!")
elif num > int(num) + 0.5:
    Rnum = int(num) + 1
    print(num, "is", Rnum, "when rounded off!")
else:
    Rnum = int(num)
    print(num, "is", Rnum, "when rounded off!")