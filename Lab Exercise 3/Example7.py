#Example No. 7

a=int(input("Your first value is :",))
b=int(input("Your second value is :",))
c=int(input("Your third value is :",))
if a>b and a>c:
    print("The largest number is",a)
elif b>a and b>c:
        print("The largest number is",b)
else:
    print("The largest number is",c)
