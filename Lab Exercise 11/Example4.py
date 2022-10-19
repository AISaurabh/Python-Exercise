#Example No. 4
#Replace all occurrences of 5 with five for the given string
#i.e. 'They ate 5 apples and 5 oranges' 
import re
a='They ate 5 apples and 5 oranges'
print(a)
print("The updated sentence is :")
print(re.sub('5','five','They ate 5 apples and 5 oranges')) 
