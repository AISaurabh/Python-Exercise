#Example No. 18
#18: Write a python program to print following multiplication table on the screen



for i in range(1,11):
    print("\t",i,end=" ")
print("\n   +---------------------------------------------------------------------------------")
for j in range(1,11):
    if j<10:
        print(" ",end="")
    print(j,"| ",end="\t")
    for i in range(1,11):
            print(i*j,end="\t")
    print()

    
