Given a employees and departments table, select the top 3 departments with at least ten employees and rank them according to the percentage of their employees making over 100K in salary.

Example:

Input:

employees table

Columns	Type
id	INTEGER
first_name	VARCHAR
last_name	VARCHAR
salary	INTEGER
department_id	INTEGER
departments table

Columns	Type
id	INTEGER
name	VARCHAR
Output:

Column	Type
percentage_over_100k	FLOAT
department_name	VARCHAR
number_of_employees	INTEGER



// one

SELECT 
       d.name, 
      SUM(CASE WHEN e.salary > 100000 THEN 1 ELSE 0 END)/COUNT(DISTINCT e.id)AS pct_above_100k,
      COUNT(DISTINCT e.id) AS c
FROM employees e JOIN departments d ON e.department_id = d.id
GROUP BY 1
HAVING COUNT(*) >=10
ORDER BY 2 DESC
LIMIT 3



// two


select 
    d.name as department_name,
    count(distinct e.id) as number_of_employees,
    sum(case when e.salary > 100000 then 1 else 0 
    end)/count(distinct e.id) as percentage_over_100k
from 
    departments d 
left join 
    employees e 
on 
    d.id = e.department_id
group by 
    d.id
having 
    count(distinct e.id) >= 10
limit 3