#Example No. 10
import sys
x= ['a',2]

for i in x:
    try:
        print("The entry is :",i)
        r = 5/(i)
        break
    except:
        print("sorry!", sys.exc_info()[0], "occurred.")
        print()
print("The reciprocal of",i, "is", r)
