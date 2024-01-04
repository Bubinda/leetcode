SELECT email
FROM employee_email
GROUP BY email
HAVING COUNT(email) > 1;




-- also solved by check for same email with different id


SELECT e1.email_address
FROM emails e1
JOIN emails e2 ON e1.email_address = e2.email_address AND e1.id <> e2.id;


