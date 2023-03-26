#Example No. 8
#Q8: a Python program to get a string from a given string where all occurrences
#of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'



a="restart"
print(a[:5]+'$'+a[-1:])
