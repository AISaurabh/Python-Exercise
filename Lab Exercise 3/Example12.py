#Exercise No. 12

list1=[5,10,15,20,25,50,20]
a=list1.index(20)
list1=list1[:a]+[200]+list1[a+1:]
print("The updated list is",list1)
