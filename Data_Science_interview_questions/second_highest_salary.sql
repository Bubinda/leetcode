SELECT DISTINCT base_salary AS „Second Highest Salary“
FROM employee 
ORDER BY base_salary DESC
LIMIT 1 OFFSET 1



-- # Instead of DISTINCT we can also use GROUP BY clause


SELECT base_salary AS "Second Highest Salary"
FROM employee
GROUP BY base_salary
ORDER BY base_salary DESC
LIMIT 1 OFFSET 1;


-- # or without both of them and using the fact that the second-highest salary is one step lower than the overall max salary

SELECT MAX(base_salary) AS "Second Highest Salary"
FROM employee
WHERE base_salary < (SELECT MAX(base_salary) FROM employee);

