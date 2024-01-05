-- Find the top three distinct salaries for each department. Output the department name and the top 3 distinct salaries by each department. Order your results alphabetically by department and then by highest salary to lowest.

-- twitter_employee


-- id: int
-- first_name: varchar
-- last_name: varchar
-- age: int
-- sex: varchar
-- employee_title: varchar
-- department: varchar
-- salary: int
-- target: int
-- bonus: int
-- email: varchar
-- city: varchar
-- address: varchar
-- manager_id: int



WITH ranked_salaries AS (
    SELECT
        department,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
    FROM twitter_employee
)
SELECT
    department,
    salary
FROM ranked_salaries
WHERE salary_rank <= 3
ORDER BY department, salary DESC;
