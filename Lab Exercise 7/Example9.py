#Example No. 9
from datetime import datetime,timedelta
a=datetime.today()
print("The current date is :",a)
for i in range(9):
    a+=timedelta(weeks=1)
    print("After a week the date is :",a)

