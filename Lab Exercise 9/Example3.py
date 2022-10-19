#Example No. 3
class staff:
    def __init__(self):
        self.name =input("Enter your name :")
        self.code =input("Enter staff code :")
    def name_code(self):
        print("your name is :",self.name)
        print("staff code is :",self.code)
class teacher(staff):
    def __init__(self):
        staff.__init__(self)
        self.subject =input("Enter subject name :")
        self.publication=input("Enter publication name :")
    def subject_publication(self):
        print("subject name is :",self.subject)
        print("publication name is :",self.publication)
class typist(staff):
    def __init__(self):
        staff.__init__(self)
        self.speed =input("Enter typing speed in words/minute :")
    def speed_typing(self):
        print("The typing speed is :",self.speed)
class officer(staff):
    def __init__(self):
        staff.__init__(self)
        self.grade=input("Enter the grade :")
    def grade_officer(self):
        print("The officer's grade is :",self.grade)
class regular(typist):
    def __init__(self):
        typist.__init__(self)
        self.salary =int(input("Enter salary of regular typist:"))
    def salary_regular(self):
        print("Regular typist's salary is :",self.salary)
class casual(typist):
    def __init__(self):
        typist.__init__(self)
        self.daily_wages=int(input("Enter salary of casual typist:"))
    def dailywages(self):
        print("Casual typist's daily wages is :",self.daily_wages)
print("1.teacher","\n","2.officer","\n","3.Regular typist","\n","4.Casual typist","\n","5.Exit")
x=0
while x!=5:
    x=int(input("Enter your choice :"))
    if x==1:
        t=teacher()
        t.name_code()
        t.subject_publication()
    elif x==2:
        o=officer()
        o.name_code()
        o.grade_officer()
    elif x==3:
        a=regular()
        a.speed_typing()
        a.salary_regular()
    elif x==4:
        b=casual()
        b.speed_typing()
        b.dailywages()
else:
    print("EXIT")
        
    

