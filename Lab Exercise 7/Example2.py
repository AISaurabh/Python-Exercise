#Example No. 2
#C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab Exercise 7\Lab7text.txt
a=input("Enter the directory:")
b=open(a,mode="a+")
b.write("\nWelcome to CDAC NOIDA")
b.seek(0)
print(b.read())
b.close()

