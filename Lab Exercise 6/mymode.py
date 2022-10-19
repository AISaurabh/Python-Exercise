#Example No. 2
f=(r"C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Lab Exercise 6\Text.txt")
def countline(f):
    a=open(f)
    b=a.readlines()
    print("Number of lines are:",len(b))
    a.close()
countline(f)

def countchar(f):
    c=open(f)
    d=len(c.read())
    print("Number of characters are:",d)
    c.close()
countchar(f)

def test(f):
    countline(f)
    countchar(f)
test(f)
    
print(__name__)
if(__name__=="__main__"):
    test(f)
else:
    print("Do not call test function")
