#Example No. 5
#Q5: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string is already ends with 'ing' then add 'ly' instead.


a=str(input("The string is :",))
if (len(a)>=3):
    if (a[-3:]=='ing'):
        a=a+'ly'
        print("The string is :",a)
    else:
        a=a+'ing'
        print("The string is:",a)
