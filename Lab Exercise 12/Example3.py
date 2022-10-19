# Example No. 3

import cx_Oracle
con=cx_Oracle.connect("system/Cdac1234@localhost:1521/orcl")
cursor=con.cursor()

#a. List the names of all clients having ‘a’ as the second letter in their names.
cursor.execute("Select name from CLIENT_MASTER where name like'_a%'")
a=cursor.fetchall()
print(a[:],"this all clients having ‘a’ as the second letter in their names.")

#b. List the clients who stay in a city whose first letter is ‘M’.
cursor.execute("Select * from CLIENT_MASTER where city like'M%'")
a=cursor.fetchall()
print(a[:],"this clients who stay in a city whose first letter is ‘M’.")

#c. List all clients who stay in ‘Bangalore’ or ‘Mangalore’.
cursor.execute("Select * from CLIENT_MASTER where city='Bangalore' OR city='Mangalore'")
a=cursor.fetchall()
print(a[:],"this are  clients who stay in ‘Bangalore’ or ‘Mangalore’.")

#d. List all clients whose BalDue is greater than value 10000.
cursor.execute("Select * from CLIENT_MASTER where  BALDUE > 10000")
a=cursor.fetchall()
print(a[:],"this are clients whose BalDue is greater than value 10000.")

#e. List all information from the Sales_order table for order placed in the month of June.
cursor.execute("Select * from SALES_ORDER where EXTRACT (MONTH FROM ORDER_DATE) = '06'") 
a=cursor.fetchall()
print(a[:],"this are the order placed in the month of June.")

#f. List the Order No & day on which clients placed their order.
cursor.execute("Select ORDER_NO, EXTRACT(DAY FROM ORDER_DATE) from SALES_ORDER")
a=cursor.fetchall()
print(a[:],"this are Order No & day on which clients placed their order." )

#g. List the names, city and state of clients who are not in the state of ‘Maharashtra’.
cursor.execute("Select NAME, CITY, STATE FROM CLIENT_MASTER WHERE STATE != 'Maharashtra'")
a=cursor.fetchall()
print(a[:],"this are the names, city and state of clients who are not in the state of ‘Maharashtra’.")
    
cursor.close()
con.close()

