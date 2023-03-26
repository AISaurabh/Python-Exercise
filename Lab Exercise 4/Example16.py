#Example No. 16
#Q16: WAP to print the following asterisk pattern:
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *



for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")    

#n = int(input("row:"))
#for i in range(1,n+1):
    #print(' * '* i)
    
