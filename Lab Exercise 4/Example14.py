#Example No. 14
#Q 14: write a Program to Remove Punctuations from a String provided by the user. [Hint: use 
#punctuation attribute of string module to get all punctuations (i.e. !"#$%&\'()*+,-
#./:;<=>?@[\\]^_`{|}~ ) ]


import string
a=str(input("Enter your string:"))
b=string.punctuation
for i in a:
    if i in b:
        a=a.replace(i,"")
print(a)   
