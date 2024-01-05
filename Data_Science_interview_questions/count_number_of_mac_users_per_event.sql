-- Count the number of user events performed by MacBookPro users.
-- Output the result along with the event name.
-- Sort the result based on the event count in the descending order.
-- Table: playbook_events
-- Hints
-- Expected Output
-- playbook_events

-- Preview
-- user_id: int
-- occurred_at: datetime
-- event_type: varchar
-- event_name: varchar
-- location: varchar
-- device: varchar


-- soulution 1

SELECT 
    event_name,
    SUM(CASE WHEN device = 'MacBookPro' THEN 1 END) AS number_of_mac_user
FROM playbook_events
GROUP BY event_name
ORDER BY number_of_mac_user DESC;


-- solution 2

SELECT
    event_name,
    COUNT(*) AS event_count
FROM playbook_events
WHERE device = 'MacBookPro'
GROUP BY event_name
ORDER BY event_count DESC;
