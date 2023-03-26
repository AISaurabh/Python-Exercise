#Example No. 12
#Q12: Program to count the number of each vowel in a string


a=str(input("Enter the string :",))
b='aeiouAEIOU'
count={}.fromkeys(b,0) 
for i in b:
    for j in a:
        if i==j:
            count[i]+=1
print("The expected output is",count)
