#Example No. 9
#Q9: write a Program to check if a string is palindrome or not


a=str(input("Your string is :"))
if a[::-1]==a:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")
