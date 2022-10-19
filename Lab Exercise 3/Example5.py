#Example No. 5

a=str(input("The string is :",))
if (len(a)>=3):
    if (a[-3:]=='ing'):
        a=a+'ly'
        print("The string is :",a)
    else:
        a=a+'ing'
        print("The string is:",a)
