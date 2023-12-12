Given a table with event logs, find the percentage of users that had at least one seven-day streak of visiting the same URL.

Note: Round the results to 2 decimal places. For example, if the result is 35.67% return 0.35.

Example:

Input:

events table

Column	Type
user_id	INTEGER
created_at	DATETIME
url	VARCHAR
Output

Column	Type
percent_of_users	FLOAT





WITH UserStreaks AS (
    SELECT
        user_id,
        url,
        created_at,
        LAG(created_at) OVER (PARTITION BY user_id, url ORDER BY created_at) AS prev_visit
    FROM
        events
)
SELECT
    ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM events), 2) AS percent_of_users
FROM
    UserStreaks
WHERE
    DATEDIFF(created_at, prev_visit) <= 7 OR prev_visit IS NULL;
