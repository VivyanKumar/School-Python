R = input("Input your amount in rupees: (for example; 3.74)")
if R.rfind('.') >= 0:
    r = R[0:R.rfind('.')]
    p = R[R.rfind('.')+1:(R.rfind('.')+3)]
    print("You have", r, "rupees and", p, "paise!")
else:
    print("Invalid Input")