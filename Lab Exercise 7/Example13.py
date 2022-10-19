#Example No. 13
from datetime import datetime,timedelta
a=datetime.today()
b=(a-datetime(a.year,1,1))
print("The day of year is :",b)
