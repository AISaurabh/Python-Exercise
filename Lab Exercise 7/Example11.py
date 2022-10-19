#Example No. 11
from datetime import datetime,timedelta
a=datetime.today()
b=datetime(2022,1,1)
print("Current date and time is :",a)
print("Current year in full is :",(a.year))
print("Month of year full name is :",a.strftime("%B"))
print("Weekday of the week is :",a.strftime("%w"))
print("The day of year is :",a-b)
print("The day of month is :",a.strftime("%d"))
print("The day of week in full name is :",a.strftime("%A"))
