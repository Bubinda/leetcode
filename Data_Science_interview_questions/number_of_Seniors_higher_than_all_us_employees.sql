-- Find whether the number of senior workers (i.e., more experienced) at Meta/Facebook is higher than number of USA based employees at Facebook/Meta.
-- If the number of seniors is higher then output as 'More seniors'. Otherwise, output as 'More USA-based'.


-- id: int
-- location: varchar
-- age: int
-- gender: varchar
-- is_senior: bool


SELECT 
    CASE 
        WHEN SUM(CASE WHEN is_senior = true THEN 1 END) > SUM(CASE WHEN location = 'USA' THEN 1 END) 
            THEN 'More seniors'
        ELSE 'More USA-based'
    END AS result
FROM employees;




-- SELECT 
--     CASE 
--         WHEN COUNT(is_senior = true) > COUNT(location = 'USA') 
--             THEN 'More seniors'
--         ELSE 'More USA-based'
--     END AS result
-- FROM employees;



SELECT
    CASE 
        WHEN n_seniors > n_usa_based
            THEN 'More seniors'
        ELSE 'More USA-based'
    END AS winner
FROM
    (SELECT
        SUM(CASE WHEN is_senior THEN 1 ELSE 0 END) AS n_seniors
    FROM
        employees) seniors
LEFT JOIN
    (SELECT
        COUNT(*) AS n_usa_based
    FROM
        employees
    WHERE
        location = 'USA'
    ) us_based
ON TRUE
