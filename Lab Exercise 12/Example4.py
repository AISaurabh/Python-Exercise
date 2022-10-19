#Example No. 4

import cx_Oracle
con=cx_Oracle.connect("system/Cdac1234@localhost:1521/orcl")
cursor=con.cursor()

#a. Printing the description and total quantity sold for each product.
cursor.execute("SELECT DESCRIPTION,SUM(QTYDISP) FROM PRODUCT_MASTER ,SALES_ORDER_DETAILS  WHERE PRODUCT_MASTER.PRODUCT_NO = SALES_ORDER_DETAILS.PRODUCT_NO GROUP BY DESCRIPTION")              
a=cursor.fetchall()
print(a[:],"this are the description and total quantity sold for each product.")




#b. Calculating the average quantity sold for each client that has a maximum order value of 15000.00.
cursor.execute("Select client_master.client_name,avg(sales_order_details.QTYDISP)as avg_so,max(sales_order_details.QTYORDERED*sales_order_details.PRODUCTRATE)as amt from sales_order_details join sales_order on sales_order_details.order_no=sales_order.order_no join client_master on sales_order.client_no=client_master.client_no group by client_master.client_name having amt>15000")
a=cursor.fetchall()
print(a[:],"this are the average quantity sold for each client that has a maximum order value of 15000.00")


cursor.close()
con.close()
