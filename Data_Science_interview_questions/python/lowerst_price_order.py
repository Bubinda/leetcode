# “Find the lowest order cost of each customer. Output the customer id along with the first name and the lowest order price.”


import pandas as pd
import numpy as np

# first get the join/merge of the cutsomer and the order table -> inner join from customers to orders so no costomer without an order is selected
merge = pd.merge(customers, orders, left_on="id", right_on="cust_id")

# then gourp the new table b<y the customer id and the first name and get the min of the total order cost / reset index to gehtt he old index column out of the result
result = merge.groupby(["cust_id", "first_name"])
result = result["total_order_cost"].min()
result = result.reset_index()
#those three lines above could be written as one, but with the three line the whole code is probably more readable