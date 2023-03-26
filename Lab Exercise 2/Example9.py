#Example No. 9
#Q9: Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xyc abz'



a="abc"
b="xyz"
print("The solution is :","\n",(a.replace(a[:2],b[:2]),b.replace(b[:2],a[:2])))
