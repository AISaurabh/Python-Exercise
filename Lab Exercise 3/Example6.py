#Example No. 6

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
    
