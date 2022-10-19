#Example No. 6
#Write a Python program to remove leading zeros from an IP address
import re
a='216.08.094.196'
print(a)
print("The updated IP Address is")
print(re.sub('0','',a))
