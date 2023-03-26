#Example No. 6
#Q6: The marks obtained by a student in 5 different Subjects are input through a keyboard. The 
#Student gets a division as per the following rules.
#1. Percentage above or equal to 60 – First Division
#2. Percentage between 50 and 59 – Second Division
#3. Percentage between 40 and 49 – Third Division
#4. Percentage less than 40 – Fail
#Write a python program to Display the result based on the above Criteria


a=int(input("The marks of Mathematics is :",))
b=int(input("The marks of English is :",))
c=int(input("The marks of Chemistry is :",))
d=int(input("The marks of physics is :",))
e=int(input("The marks of Economics is :",))
x=((a+b+c+d+e)/500)*100
if x>=60:
    print("Congratulations you are pass with First division")
elif 50<= x <=59:
    print("Congratulations you are pass with Second division")
elif 40<= x <=49:
    print("Congratulations you are pass with Third division")
else:
    print("Sorry you are Fail")
    
