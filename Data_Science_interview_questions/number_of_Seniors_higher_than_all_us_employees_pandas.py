# -- Find whether the number of senior workers (i.e., more experienced) at Meta/Facebook is higher than number of USA based employees at Facebook/Meta.
# -- If the number of seniors is higher then output as 'More seniors'. Otherwise, output as 'More USA-based'.


# -- id: int
# -- location: varchar
# -- age: int
# -- gender: varchar
# -- is_senior: bool



import pandas as pd

# Assuming you have a DataFrame named 'employees'
# Replace this with your actual DataFrame and column names

# Sample data
employees_data = {
    'id': [1, 2, 3, 4, 5],
    'location': ['USA', 'Canada', 'USA', 'Canada', 'Germany'],
    'age': [30, 40, 50, 35, 45],
    'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'is_senior': [True, False, True, False, True]
}

employees = pd.DataFrame(employees_data)

# Count the number of senior workers and USA-based employees
senior_count = employees['is_senior'].sum()
usa_count = (employees['location'] == 'USA').sum()

# Determine the result based on the counts
result = 'More seniors' if senior_count > usa_count else 'More USA-based'

print(result)
