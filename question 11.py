R = str(input("Input your amount in rupees: (for example; 3.74)"))
dec = '.'
if R.rfind(dec) >= 0:
    r = R[0:R.rfind(dec)]
    p = R[R.rfind(dec)+1:(R.rfind(dec)+3)]
    print("You have", r, "rupees and", p, "paise!")
else:
    print("Invalid Input")