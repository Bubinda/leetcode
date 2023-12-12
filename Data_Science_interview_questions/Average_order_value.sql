Given three tables, representing customer transactions and customer attributes:

Write a query to get the average order value by gender.

Note: We’re looking at the average order value by users that have ever placed an order. Additionally, please round your answer to two decimal places.

Example:

Input:

transactions table

Column	Type
id	INTEGER
user_id	INTEGER
created_at	DATETIME
product_id	INTEGER
quantity	INTEGER
users table

Column	Type
id	INTEGER
name	VARCHAR
sex	VARCHAR
products table

Column	Type
id	INTEGER
name	VARCHAR
price	FLOAT
Output:

Column	Type
sex	VARCHAR
aov	FLOAT




SELECT u.sex, ROUND(AVG(t.quantity * p.price), 2) AS aov
FROM users u
JOIN transactions t ON u.id = t.user_id
JOIN products p ON t.product_id = p.id
GROUP BY u.sex;