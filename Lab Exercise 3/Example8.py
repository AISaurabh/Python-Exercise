#Example No. 8

a=int(input("The input year is :",))
if a%4==0 and a%100!=0:
    print("This is a leap year")
elif a%100==0 and a%400==0:
        print("This is a leap year")
    
else:
    print("This is not a leap year")
        
