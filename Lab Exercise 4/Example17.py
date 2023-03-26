#Example No. 17
#Q17: WAP to create a function traiangle to print the following asterisk triangle pattern:
#*
#**
#***
#****
#***
#**
#*


#for i in range (1,5):
    #for j in range(1,i+1):
        #print("*",end=" ")
    #print(" ")

#for i in range (3,0,-1):
    #for j in range(i,0,-1):
        #print("*",end=" ")
    #print(" ")    

a = []
for i in range(1,5):
    print('* '* i)
    a.append('* '* i)
del a[-1]
for j in a[::-1]:
    print(j)
