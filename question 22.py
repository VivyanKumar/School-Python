char = str(input("Input the character or string you wish to convert to ASCII code: "))
for i in range(0,len(char)):
    a = char[i]
    aa = ord(a)
    print("The ASCII code value of", a, "is", ord(a))