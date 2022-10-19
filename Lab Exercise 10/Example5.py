#Example No. 5
import sys
try:
    
    a = int(input("Enter a non-zero integer: "))
    
    if a==0:
        raise ZeroDivisionError("Oops! That is not a non-zero number!")
    else:
        print(2/a)
except ZeroDivisionError as ze:
    print(ze)


