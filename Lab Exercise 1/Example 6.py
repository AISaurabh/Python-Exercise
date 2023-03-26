#Example no.6
#Q6: Write a Python Program to find the area of triangle
# Three sides of the triangle a, b and c are provided by the user


import math
a=float(input('Side a of triangle is :'))
b=float(input('side b of triangle is :'))
c=float(input('side c of triangle is :'))
s=(a+b+c)/2
area=(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print('Area of triangle is ',area)
