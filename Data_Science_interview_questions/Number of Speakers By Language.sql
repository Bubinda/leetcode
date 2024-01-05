-- Find the number of speakers of each language by country. Output the country, language, and the corresponding number of speakers. Output the result based on the country in ascending order.
-- Tables: playbook_events, playbook_users
-- Hints
-- Expected Output


-- playbook_events

-- user_id: int
-- occurred_at: datetime
-- event_type: varchar
-- event_name: varchar
-- location: varchar
-- device: varchar


-- playbook_users

-- user_id: int
-- created_at: datetime
-- company_id: int
-- language: varchar
-- activated_at: datetime
-- state: varchar


SELECT 
    e.location AS country,
    u.language, 
    count(*) AS speaker_count
FROM 
    playbook_users u JOIN playbook_events e
    ON u.user_id = e.user_id
GROUP BY
    e.location, u.language
ORDER BY
    e.location ASC, speaker_count DESC;