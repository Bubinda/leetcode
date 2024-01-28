We have a table called song_plays that tracks each time a user plays a song.

Write a query to return the number of songs played on each date for each user

NOTE: If a user played the same song twice during the day count should be two.

song_plays table

column	type
id	INTEGER
date_played	DATETIME
user_id	INTEGER
song_id	INTEGER
Output:

Column	Type
user_id	INTEGER
played_date	DATE
number_of_plays	INTEGER



SELECT
    user_id,
    DATE(date_played) AS played_date,
    COUNT(*) AS number_of_plays
FROM
    song_plays
GROUP BY
    user_id,
    played_date;
