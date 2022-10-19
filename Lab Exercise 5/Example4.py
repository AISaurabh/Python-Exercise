#Example No. 4
def rec_fibo(n):
    if n<=1:
        return n
    else:
        return (rec_fibo(n-1)+rec_fibo(n-2))
a=int(input("Enter the fibinacci series:"))
if a<=0:
    print("Enter the positive integer")
else:
    print("Fibonacci series is:")
    for i in range(a):
        print(rec_fibo(i),end=' ')
