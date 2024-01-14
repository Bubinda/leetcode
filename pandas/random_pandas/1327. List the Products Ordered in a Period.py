# -- Table: Products

# -- +------------------+---------+
# -- | Column Name      | Type    |
# -- +------------------+---------+
# -- | product_id       | int     |
# -- | product_name     | varchar |
# -- | product_category | varchar |
# -- +------------------+---------+
# -- product_id is the primary key (column with unique values) for this table.
# -- This table contains data about the company's products.
 

# -- Table: Orders

# -- +---------------+---------+
# -- | Column Name   | Type    |
# -- +---------------+---------+
# -- | product_id    | int     |
# -- | order_date    | date    |
# -- | unit          | int     |
# -- +---------------+---------+
# -- This table may have duplicate rows.
# -- product_id is a foreign key (reference column) to the Products table.
# -- unit is the number of products ordered in order_date.
 

# -- Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

# -- Return the result table in any order.

# -- The result format is in the following example.

 

# -- Example 1:

# -- Input: 
# -- Products table:
# -- +-------------+-----------------------+------------------+
# -- | product_id  | product_name          | product_category |
# -- +-------------+-----------------------+------------------+
# -- | 1           | Leetcode Solutions    | Book             |
# -- | 2           | Jewels of Stringology | Book             |
# -- | 3           | HP                    | Laptop           |
# -- | 4           | Lenovo                | Laptop           |
# -- | 5           | Leetcode Kit          | T-shirt          |
# -- +-------------+-----------------------+------------------+
# -- Orders table:
# -- +--------------+--------------+----------+
# -- | product_id   | order_date   | unit     |
# -- +--------------+--------------+----------+
# -- | 1            | 2020-02-05   | 60       |
# -- | 1            | 2020-02-10   | 70       |
# -- | 2            | 2020-01-18   | 30       |
# -- | 2            | 2020-02-11   | 80       |
# -- | 3            | 2020-02-17   | 2        |
# -- | 3            | 2020-02-24   | 3        |
# -- | 4            | 2020-03-01   | 20       |
# -- | 4            | 2020-03-04   | 30       |
# -- | 4            | 2020-03-04   | 60       |
# -- | 5            | 2020-02-25   | 50       |
# -- | 5            | 2020-02-27   | 50       |
# -- | 5            | 2020-03-01   | 50       |
# -- +--------------+--------------+----------+
# -- Output: 
# -- +--------------------+---------+
# -- | product_name       | unit    |
# -- +--------------------+---------+
# -- | Leetcode Solutions | 130     |
# -- | Leetcode Kit       | 100     |
# -- +--------------------+---------+
# -- Explanation: 
# -- Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
# -- Products with product_id = 2 is ordered in February a total of 80.
# -- Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
# -- Products with product_id = 4 was not ordered in February 2020.
# -- Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.


import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Convert 'order_date' to datetime type
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    # Filter orders for the year 2020 and month 2
    filtered_orders = orders[(orders['order_date'].dt.year == 2020) & (orders['order_date'].dt.month == 2)]

    # Join Products and filtered Orders
    merged_df = pd.merge(products, filtered_orders, on='product_id')

    # Group by 'product_id' and 'product_name', summing 'unit'
    grouped_df = merged_df.groupby(['product_id', 'product_name']).agg({'unit': 'sum'}).reset_index()

    # Filter by units >= 100 using HAVING clause
    result_df = grouped_df[grouped_df['unit'] >= 100]

    result_df = result_df.rename(columns={'product_name': 'product_name', 'unit': 'unit'})

    return result_df[['product_name', 'unit']]