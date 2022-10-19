#Example No.8
import sys
try:
    a=(r"C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab Exercise 7\Lab7text.txt")
    L=["sunday","monday","tuesday"]
    b=open(a,mode="r")
    for i in L:
        b.write(i+"\n")
    b.close()
except:
    print("The given file is not writable")
