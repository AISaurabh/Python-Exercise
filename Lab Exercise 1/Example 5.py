#Example No. 5
#Q5: Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0
# Coeffients a, b and c are provided by the user

#[Hint: import complex math module - import cmath]




import cmath
a=int(input('Enter the coefficient of a:'))
b=int(input('Enter the coefficient of b:'))
c=int(input('Enter the coefficient of c:'))
s1=(-b+cmath.sqrt(b**2-4*a*c))/2*a
s2=(-b-cmath.sqrt(b**2-4*a*c))/2*a
print('The solution of s1 is ',s1,"\n" 'The solution of s2 is ',s2)

      
