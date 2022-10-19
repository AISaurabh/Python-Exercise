#Example No. 5
#C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab Exercise 7\Lab7text.txt
a=input("Enter the directory:")
L=["sunday","monday","tuesday"]
b=open(a,mode="w")
for i in L:
    b.write(i+"\n")
b.close()


