# -- +-------------+---------+
# -- | Column Name | Type    |
# -- +-------------+---------+
# -- | empId       | int     |
# -- | name        | varchar |
# -- | supervisor  | int     |
# -- | salary      | int     |
# -- +-------------+---------+
# -- empId is the column with unique values for this table.
# -- Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
 

# -- Table: Bonus

# -- +-------------+------+
# -- | Column Name | Type |
# -- +-------------+------+
# -- | empId       | int  |
# -- | bonus       | int  |
# -- +-------------+------+
# -- empId is the column of unique values for this table.
# -- empId is a foreign key (reference column) to empId from the Employee table.
# -- Each row of this table contains the id of an employee and their respective bonus.
 

# -- Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

# -- Return the result table in any order.

# -- The result format is in the following example.

 

# -- Example 1:

# -- Input: 
# -- Employee table:
# -- +-------+--------+------------+--------+
# -- | empId | name   | supervisor | salary |
# -- +-------+--------+------------+--------+
# -- | 3     | Brad   | null       | 4000   |
# -- | 1     | John   | 3          | 1000   |
# -- | 2     | Dan    | 3          | 2000   |
# -- | 4     | Thomas | 3          | 4000   |
# -- +-------+--------+------------+--------+
# -- Bonus table:
# -- +-------+-------+
# -- | empId | bonus |
# -- +-------+-------+
# -- | 2     | 500   |
# -- | 4     | 2000  |
# -- +-------+-------+
# -- Output: 
# -- +------+-------+
# -- | name | bonus |
# -- +------+-------+
# -- | Brad | null  |
# -- | John | null  |
# -- | Dan  | 500   |
# -- +------+-------+



# solution with merge and condition
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, how='left', on='empId')
    # merged = employee.merge(bonus, left_on='empId', right_on='empId', how='left')
    less_bonus = merged[(merged['bonus'] < 1000) | (merged['bonus'].isna())]
    return less_bonus[['name', 'bonus']]


# solution with conditional drop
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    combined = pd.merge(employee, bonus, how = 'left', on = 'empId')
    combined = combined[['name', 'bonus']]
    combined = combined.drop(combined[combined.bonus >= 1000].index)
    return combined