#Example No. 10
#Q10: write a Program to sort alphabetically the words form a string provided by the user. [You 
#can use split() method to split string into a list of words. ]


a=str(input("The given string is :"))
b=a.split()
b.sort()
c=b
print("The solution is :",c)
