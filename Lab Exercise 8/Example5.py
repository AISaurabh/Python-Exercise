#Example No. 5
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
l=int(input("Enter length of a rectangle :"))
b=int(input("Enter breadth of a rectangle :"))
print("1.Area")
print("2.Perimeter")
print("3.Exit")
r=rectangle(l,b)
x=0
while x!=3:
    x=int(input("Enter your choice :"))
    if (x==1):
        print("Area of rectangle with length",l,"and breadth",b,"is",r.area())
    elif (x==2):
        print("Perimeter of rectangle with length",l,"and breadth",b,"is",r.perimeter())
else:
    print("End of program")
