#Example No. 1
#C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab7text.txt
a=input("Enter the directory:")
n=int(input("Enter the number of lines:"))
b=open(a,mode="r")
c=b.readlines()
for i in range(0,n):
    print(c[i],end=" ")
b.close()
