# -- Find the top three distinct salaries for each department. Output the department name and the top 3 distinct salaries by each department. Order your results alphabetically by department and then by highest salary to lowest.

# -- twitter_employee


# -- id: int
# -- first_name: varchar
# -- last_name: varchar
# -- age: int
# -- sex: varchar
# -- employee_title: varchar
# -- department: varchar
# -- salary: int
# -- target: int
# -- bonus: int
# -- email: varchar
# -- city: varchar
# -- address: varchar
# -- manager_id: int


import pandas as pd

# Assuming you have a DataFrame named 'df' with columns 'department' and 'salary'
# Replace this with your actual DataFrame and column names

# Sample data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'first_name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'David', 'Paul', 'Tom', 'Kevin'],
    'department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'IT', 'IT', 'CFO'],
    'salary': [60000, 75000, 60000, 80000, 90000, 85000, 100000, 52200, 900000]
}

df = pd.DataFrame(data)

# Use rank to assign a rank to each salary within each department
df['salary_rank'] = df.groupby('department')['salary'].rank(ascending=False, method='dense')

# Select the top three distinct salaries for each department
top_salaries = df[df['salary_rank'] <= 3][['department', 'salary']].sort_values(by=['department', 'salary'], ascending=[True, False])

print(top_salaries)
