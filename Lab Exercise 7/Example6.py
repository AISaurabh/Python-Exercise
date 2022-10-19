#Example No. 6
a=input("Enter the directory:")
b=open(a,mode="r")
numwords = 0
numchars = 0
numlines = 0

   
for line in b:
    wordlist = line.split()
    numlines += 1
    numwords += len(wordlist)
    numchars += len(line)
print("Lines:", numlines)
print("Words:", numwords)
print("Characters:", numchars)
b.close()


























