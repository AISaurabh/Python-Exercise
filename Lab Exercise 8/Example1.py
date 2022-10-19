#Example No. 1
class Triangle:
    number_of_sides = 3
    def __init__(self,a,b,c):
        self.angle_1=a
        self.angle_2=b
        self.angle_3=c
        result=self.angle_1+self.angle_2+self.angle_3
        print(result)

    def check_angles(self,a,b,c):
        
        if (a+b+c==180):
            print("True")
        else:
            print("False")

t=Triangle(90,30,60)




