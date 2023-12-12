Given a table of product subscriptions with a subscription start date and end date for each user, write a query that returns true or false whether or not each user has a subscription date range that overlaps with any other completed subscription.

Completed subscriptions have end_date recorded.

Example:

Input:

subscriptions table

Column	Type
user_id	INTEGER
start_date	DATETIME
end_date	DATETIME
user_id	start_date	end_date
1	2019-01-01	2019-01-31
2	2019-01-15	2019-01-17
3	2019-01-29	2019-02-04
4	2019-02-05	2019-02-10
Output:

user_id	overlap
1	1
2	1
3	1
4	0







SELECT
    s1.user_id
    , MAX(CASE WHEN s2.user_id IS NOT NULL THEN 1 ELSE 0 END) AS overlap
FROM subscriptions AS s1
LEFT JOIN subscriptions AS s2
    ON s1.user_id != s2.user_id
        AND s1.start_date <= s2.end_date
        AND s1.end_date >= s2.start_date
GROUP BY 1