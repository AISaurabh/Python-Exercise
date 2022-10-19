#Example No. 2
class person:
    def __init__(self,name,code):
        self.name = name
        self.code = code

class account(person):
    def __init__(self,name,code,pay):
        person. __init__(self,name,code)
        self.pay = pay
class admin(person):
    def __init__(self,name,code,experience):
        person. __init__(self,name,code)
        self.experience = experience

class employee(account,admin):
    def __init__(self,name,code,experience,pay):
        account. __init__(self,name,code,pay)
        admin.__init__(self,name,code,experience)

c1=employee("Saurabh",1234,"2 Years",1200000)
print(c1.name,"\n",c1.code,"\n",c1.experience,"\n",c1.pay)
        
        
         
