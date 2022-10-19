#Example No. 2
#Write a Python program to check for a number at the end of a string.
import re
a=input("Enter the string :")
b=re.compile("[0-9]$")
c=re.search(b,a)
if c:
    print("The number is present at the end of string")
else:
    print("The number is not present at the end of string")
    
