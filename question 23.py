def hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if ((num1 % i) == 0) and ((num2 % i) == 0):
            hcf = i
    return hcf
def lcm(num1,num2): 
    for i in range(max(num1,num2), 1 + (num1*num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            return lcm
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
print("The LCM of", num1, "and", num2, "is", lcm(num1,num2))
print("The HCF of", num1, "and", num2, "is", hcf(num1,num2))