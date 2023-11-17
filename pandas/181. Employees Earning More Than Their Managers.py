# Table: Employee

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

# Write a solution to find the employees who earn more than their managers.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+-------+--------+-----------+
# | id | name  | salary | managerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | Null      |
# | 4  | Max   | 90000  | Null      |
# +----+-------+--------+-----------+
# Output: 
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+
# Explanation: Joe is the only employee who earns more than his manager.





import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df2 = pd.DataFrame()
    df2 = employee.merge(employee, left_on = "id", right_on = "managerId", how = "inner")
    #print(df2.head())
#        id_x name_x  salary_x  managerId_x  id_y name_y  salary_y  managerId_y
# 0     3    Sam     60000         <NA>     1    Joe     70000            3
# 1     4    Max     90000         <NA>     2  Henry     80000            4
    df2 = df2[df2['salary_x'] < df2['salary_y']][['name_y']]
    df2.rename(columns={'name_y':'Employee'},inplace = True)
    return df2