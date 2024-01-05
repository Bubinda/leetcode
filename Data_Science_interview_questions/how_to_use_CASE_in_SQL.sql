SELECT
    employee_name,
    department,
    CASE department
        WHEN 'IT' THEN 'Information Technology'
        WHEN 'HR' THEN 'Human Resources'
        WHEN 'Finance' THEN 'Finance Department'
        ELSE 'Other Department'
    END AS department_description
FROM employees;



-- In this example, the CASE statement is used to create a new column called department_description based on the values in the department column. 
-- If the department is 'IT', it sets the description to 'Information Technology', 
-- if 'HR', it sets to 'Human Resources', 
-- if 'Finance', it sets to 'Finance Department', and for any other department, it sets to 'Other Department'.



SELECT
    product_name,
    units_sold,
    CASE
        WHEN units_sold > 1000 THEN 'High Sales'
        WHEN units_sold BETWEEN 500 AND 1000 THEN 'Medium Sales'
        ELSE 'Low Sales'
    END AS sales_category
FROM sales_data;



-- In this example, the CASE statement is used without a specific column to evaluate. Instead, it checks the condition directly. 
-- The sales_category column is assigned values based on the units_sold. If units_sold is greater than 1000, it's 'High Sales', 
-- if between 500 and 1000 (inclusive), it's 'Medium Sales', 
-- and otherwise, it's 'Low Sales'.