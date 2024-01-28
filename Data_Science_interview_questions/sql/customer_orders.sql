-- Write a query to identify customers who placed more than three transactions each in both 2019 and 2020.

-- Example:

-- Input:

-- transactions table

-- Column	Type
-- id	INTEGER
-- user_id	INTEGER
-- created_at	DATETIME
-- product_id	INTEGER
-- quantity	INTEGER
-- users table

-- Column	Type
-- id	INTEGER
-- name	VARCHAR
--   Output:

-- Column	Type
-- customer_name	VARCHAR




SELECT
    u.name AS customer_name
FROM
    users u
JOIN
    transactions t ON u.id = t.user_id
WHERE
    YEAR(t.created_at) IN (2019, 2020)
GROUP BY
    u.id, u.name
HAVING
    COUNT(DISTINCT CASE WHEN YEAR(t.created_at) = 2019 THEN t.id END) > 3
    AND COUNT(DISTINCT CASE WHEN YEAR(t.created_at) = 2020 THEN t.id END) > 3;
