# Example No. 1
n=int(input("Enter the number:"))
l=[0,1]
for i in range(0,n):
    l.append(l[i+1]+l[i])
print(l)
