#Example No. 1
#Write a Python program that matches a string that has an a followed
#by zero or more b's.

import re
x=input("Enter a string:")
p=re.compile("ab*",re.I)
print(p.findall(x))

