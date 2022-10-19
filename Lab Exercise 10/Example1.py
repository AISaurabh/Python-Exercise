#Example No. 1 & 3

import sys
a = [0,'a',2]

for i in a:
    try:
        print("The entry is :",i)
        r = 5/(i)
        break
    except:
        print("sorry!", sys.exc_info()[0], "occurred.")
        print()
print("The reciprocal of",i, "is", r)
