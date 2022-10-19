#Example No. 4
#C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab Exercise 7\Lab7text.txt
a=a=input("Enter the directory:")
b=open(a,mode="r")
c=b.readlines()
for i in range (0,len(c)):
    d=c[i][::-1]
    print(d)
b.close()
