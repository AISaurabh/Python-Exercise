#Example No. 8
from datetime import datetime,timedelta
given_date = datetime(2020,3,22,10,0,0)
print("The given date is: ",given_date)
days = timedelta(7,hours=12)
new_date = given_date + days
print("The new updated date is :",new_date)
