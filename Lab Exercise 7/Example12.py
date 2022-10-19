#Example No. 12
from datetime import datetime
a='Jul 1 2016  2:43AM'
print("The given date time is :",a)
print("The updated date time is :",datetime.strptime('Jul 1 2016  2:43AM',"%b %d %Y %I:%M%p"))
