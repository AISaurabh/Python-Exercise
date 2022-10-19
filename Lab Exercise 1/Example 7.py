#Example No. 7

x=int(input("Enter the five digit number :"))
sum=0
remain=x%10
sum=sum+remain
x=x//10

remain=x%10
sum=sum+remain
x=x//10

remain=x%10
sum=sum+remain
x=x//10

remain=x%10
sum=sum+remain
x=x//10

remain=x%10
sum=sum+remain

print("sum of five digit number is : ",sum)

