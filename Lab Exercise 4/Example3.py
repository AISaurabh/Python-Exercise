#Example No. 3
#Q3: Write a program to display the sum of square of the first ten even natural numbers
#// (2*2+ 4*4 + 6*6 + 8*8 + 10*10 + 12*12 + 14 * 14 + 16 * 16 + 18*18 + 20*20) 


a=[int(i**2) for i in range(21) if i%2==0]
print("The sum of square of the first ten even natural numbers is:",sum(a))
