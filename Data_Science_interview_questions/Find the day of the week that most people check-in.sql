-- Find the day of the week that most people want to check-in.
-- Output the day of the week alongside the corresponding check-incount.
-- Table: airbnb_contacts
-- Hints
-- Expected Output
-- airbnb_contacts


-- id_guest: varchar
-- id_host: varchar
-- id_listing: varchar
-- ts_contact_at: datetime
-- ts_reply_at: datetime
-- ts_accepted_at: datetime
-- ts_booking_at: datetime
-- ds_checkin: datetime
-- ds_checkout: datetime
-- n_guests: int
-- n_messages: int


SELECT
    DATENAME(WEEKDAY,ds_checkin) AS weekday
    count(*) AS checkin_counter
FROM
    airbnb_contacts
WHERE 
    ds_checkin IS NOT NULL
GROUP BY
    weekday
ORDER BY
    checkin_counter DESC;
