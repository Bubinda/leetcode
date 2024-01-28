We’re given two tables, a users table with demographic information and the neighborhood they live in and a neighborhoods table.

Write a query that returns all neighborhoods that have 0 users. 

Example:

Input:

users table

Columns	Type
id	INTEGER
name	VARCHAR
neighborhood_id	INTEGER
created_at	DATETIME
neighborhoods table

Columns	Type
id	INTEGER
name	VARCHAR
city_id	INTEGER
Output:

Columns	Type
name	VARCHAR







SELECT n.name
FROM neighborhoods AS n
LEFT JOIN users AS u
    ON n.id = u.neighborhood_id
WHERE u.id IS NULL


// second

select n.name 
from neighborhoods n
left join users u 
on n.id = u.neighborhood_id
group by 1
having count(u.id) = 0

-> // GROUP BY 1 means grouping the result set by the first column in the SELECT clause. In this case, the first column is n.name.