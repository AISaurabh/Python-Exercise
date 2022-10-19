#Example No.3
a=[int(i) for i in input("Enter the numbers:").split()]
b=list(filter(lambda b:b%13==0,a))
print("The numbers which are divisible by 13 are:",b)
