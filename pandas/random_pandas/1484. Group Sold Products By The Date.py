# -- Table Activities:

# -- +-------------+---------+
# -- | Column Name | Type    |
# -- +-------------+---------+
# -- | sell_date   | date    |
# -- | product     | varchar |
# -- +-------------+---------+
# -- There is no primary key (column with unique values) for this table. It may contain duplicates.
# -- Each row of this table contains the product name and the date it was sold in a market.
 

# -- Write a solution to find for each date the number of different products sold and their names.

# -- The sold products names for each date should be sorted lexicographically.

# -- Return the result table ordered by sell_date.

# -- The result format is in the following example.

 

# -- Example 1:

# -- Input: 
# -- Activities table:
# -- +------------+------------+
# -- | sell_date  | product     |
# -- +------------+------------+
# -- | 2020-05-30 | Headphone  |
# -- | 2020-06-01 | Pencil     |
# -- | 2020-06-02 | Mask       |
# -- | 2020-05-30 | Basketball |
# -- | 2020-06-01 | Bible      |
# -- | 2020-06-02 | Mask       |
# -- | 2020-05-30 | T-Shirt    |
# -- +------------+------------+
# -- Output: 
# -- +------------+----------+------------------------------+
# -- | sell_date  | num_sold | products                     |
# -- +------------+----------+------------------------------+
# -- | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
# -- | 2020-06-01 | 2        | Bible,Pencil                 |
# -- | 2020-06-02 | 1        | Mask                         |
# -- +------------+----------+------------------------------+
# -- Explanation: 
# -- For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
# -- For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
# -- For 2020-06-02, the Sold item is (Mask), we just return it.



import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Convert 'sell_date' to datetime if it's not already
    activities['sell_date'] = pd.to_datetime(activities['sell_date'])

    # Pandas equivalent of the SQL query
    result = activities.groupby('sell_date').agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(x.unique())))
    ).reset_index().sort_values(by='sell_date')

    return result



# similar result
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby(
        'sell_date'
    )['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()