#Example No. 7
#Q7: If a five-digit number is input through the keyboard, write a program to calculate the
#sum of its digits without using any loop. (Hint: Use the modulus operator ‘%’) 



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

