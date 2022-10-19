#Example No. 3
#Write a Python program to search some literals strings in a string. 
import re
a=input("Enter the string you want to search :")
b=input("Enter the sentence :")
if re.search(a,b):
      print(a,"found in a sentence")
else:
    print(a,"not found in a sentence")
