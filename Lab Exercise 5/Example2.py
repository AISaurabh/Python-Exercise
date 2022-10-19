#Example No. 2
a=[int(i) for i in input("Enter the number of terms :").split()]
b=list(map(lambda b:2**b,a))
print(b)
