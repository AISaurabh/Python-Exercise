# Example No. 10
#Q10: Write a Python program to print out a set containing all the colors from a list which are not 
#present in another list
#Test Data : 
#color_list_1 = set(["White", "Black", "Red"]) 
#color_list_2 = set(["Red", "Green"])

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
a=color_list_1 ^ color_list_2
print("The expected output is:",a)
