#Exercise No. 12
#Q12: Write a python program for Given a Python list, to find value 20 in the list, and if it is 
#present, replace it with 200. Only update the first occurrence of a value
#list1 = [5, 10, 15, 20, 25, 50, 20]
#Expected output:
#list1 = [5, 10, 15, 200, 25, 50, 20]


list1=[5,10,15,20,25,50,20]
a=list1.index(20)
list1=list1[:a]+[200]+list1[a+1:]
print("The updated list is",list1)
