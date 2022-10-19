#Example No.6
def decitobi(n):
    if n>1:
        decitobi(n//2)
    print(n%2, end=" ")
a=int(input("Enter the decimal number:"))
decitobi(a)
print()
        
        
    
