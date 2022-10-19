#Example No. 4
import sys
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Enter an even number!")
else:
    result = 1/num
    print(result)
