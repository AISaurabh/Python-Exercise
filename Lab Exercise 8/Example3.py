#Example No. 3
class Lunch:
    def __init__(self,menu):
        self.menu=menu
    def menu_price(self):
        if self.menu=="Menu1":
            print("Your choice menu price : 12.00")
        elif self.menu=="Menu2":
            print("Your choice menu price : 13.40")
        else:
            print("Error in menu")

a=input("Enter your menu here (Menu1/Menu2) :")
paul=Lunch(a)

