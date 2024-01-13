# -- Table: Teacher

# -- +-------------+------+
# -- | Column Name | Type |
# -- +-------------+------+
# -- | teacher_id  | int  |
# -- | subject_id  | int  |
# -- | dept_id     | int  |
# -- +-------------+------+
# -- (subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
# -- Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
 

# -- Write a solution to calculate the number of unique subjects each teacher teaches in the university.

# -- Return the result table in any order.

# -- The result format is shown in the following example.

 

# -- Example 1:

# -- Input: 
# -- Teacher table:
# -- +------------+------------+---------+
# -- | teacher_id | subject_id | dept_id |
# -- +------------+------------+---------+
# -- | 1          | 2          | 3       |
# -- | 1          | 2          | 4       |
# -- | 1          | 3          | 3       |
# -- | 2          | 1          | 1       |
# -- | 2          | 2          | 1       |
# -- | 2          | 3          | 1       |
# -- | 2          | 4          | 1       |
# -- +------------+------------+---------+
# -- Output:  
# -- +------------+-----+
# -- | teacher_id | cnt |
# -- +------------+-----+
# -- | 1          | 2   |
# -- | 2          | 4   |
# -- +------------+-----+
# -- Explanation: 
# -- Teacher 1:
# --   - They teach subject 2 in departments 3 and 4.
# --   - They teach subject 3 in department 3.
# -- Teacher 2:
# --   - They teach subject 1 in department 1.
# --   - They teach subject 2 in department 1.
# --   - They teach subject 3 in department 1.
# --   - They teach subject 4 in department 1.



import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(["teacher_id"])
    df = df["subject_id"].nunique()
    df = df.reset_index()
    df = df.rename({'subject_id': 'cnt'}, axis=1)
    return df


#Use nunique() when you want to know the count of unique values.
#Use unique() when you want to retrieve an array containing all unique values.