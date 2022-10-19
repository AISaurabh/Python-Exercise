#Example No. 5
#Replace all occurrences of note irrespective of case with X in given string
#i.e. 'This note should not be NoTeD'
import re
a='This note should not be NoTeD.'
print(a)
print("The updated sentence is :")
print(re.sub('note','x','This note should not be NoTeD.',flags=re.IGNORECASE))
