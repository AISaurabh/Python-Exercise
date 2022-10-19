#Example No. 9
import sys
try:
    a=int(input("Enter the integer :"))
    if a<0:
          raise Exception("Please enter a positive integer")
    print(a)
except Exception as e:
    print(e)
