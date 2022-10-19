#Example No. 5
def sum(n):
    if n<=1:
        return n
    else:
        return (n+sum(n-1))
a=int(input("Enter the natural number:"))
if a<=0:
    print("Enter the positive integer")
else:
    print("The sum of given natural number is :",sum(a))
