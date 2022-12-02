def reverse(x):
    return str(x[::-1])
pal = input("Input a string or number to palindrome here ")
if len(pal) == 1:
    print("The palindrome is", pal)
elif len(pal) > 1:
    print("The palindrome is", pal + reverse(pal))
else:
    print("Invalid input.")