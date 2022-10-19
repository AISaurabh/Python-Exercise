#Example No. 14

import string
a=str(input("Enter your string:"))
b=string.punctuation
for i in a:
    if i in b:
        a=a.replace(i,"")
print(a)   
