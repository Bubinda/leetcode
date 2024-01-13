# -- Table: Employee

# -- +---------------+---------+
# -- | Column Name   |  Type   |
# -- +---------------+---------+
# -- | employee_id   | int     |
# -- | department_id | int     |
# -- | primary_flag  | varchar |
# -- +---------------+---------+
# -- (employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
# -- employee_id is the id of the employee.
# -- department_id is the id of the department to which the employee belongs.
# -- primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
 

# -- Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

# -- Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

# -- Return the result table in any order.

# -- The result format is in the following example.

 

# -- Example 1:

# -- Input: 
# -- Employee table:
# -- +-------------+---------------+--------------+
# -- | employee_id | department_id | primary_flag |
# -- +-------------+---------------+--------------+
# -- | 1           | 1             | N            |
# -- | 2           | 1             | Y            |
# -- | 2           | 2             | N            |
# -- | 3           | 3             | N            |
# -- | 4           | 2             | N            |
# -- | 4           | 3             | Y            |
# -- | 4           | 4             | N            |
# -- +-------------+---------------+--------------+
# -- Output: 
# -- +-------------+---------------+
# -- | employee_id | department_id |
# -- +-------------+---------------+
# -- | 1           | 1             |
# -- | 2           | 1             |
# -- | 3           | 3             |
# -- | 4           | 3             |
# -- +-------------+---------------+
# -- Explanation: 
# -- - The Primary department for employee 1 is 1.
# -- - The Primary department for employee 2 is 1.
# -- - The Primary department for employee 3 is 3.
# -- - The Primary department for employee 4 is 3.


import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:

    # Query 1
    query1_result = (
        employee.groupby('employee_id')
        .filter(lambda x: len(x) == 1)
        .loc[:, ['employee_id', 'department_id']]
    )

    # Query 2
    query2_result = (
        employee[employee['primary_flag'] == 'Y']
        .loc[:, ['employee_id', 'department_id']]
    )

    # Combine the two queries, overwriting rows from query1 with rows from query2
    result = query1_result.set_index('employee_id').combine_first(query2_result.set_index('employee_id')).reset_index()


    return result



# simpler solution 

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
  employee['d_cnt'] = employee.groupby('employee_id').department_id.transform('count')
  return employee.query("(primary_flag == 'Y') | (d_cnt == 1)").iloc[:,[0,1]]





# very similar to the first solution

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Filter only primary departments for each employee
    primary_departments = employee[employee['primary_flag'] == 'Y'][['employee_id', 'department_id']]

    # For employees with only one department, include their non-primary department
    non_primary_departments = (
        employee.groupby('employee_id')
        .filter(lambda x: len(x) == 1)
        .loc[:, ['employee_id', 'department_id']]
    )

    # Concatenate the primary and non-primary departments
    result = primary_departments.set_index('employee_id').combine_first(non_primary_departments.set_index('employee_id')).reset_index()

    # Display the result
    return result
