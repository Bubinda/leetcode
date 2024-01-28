-- Find the top 5 cities with the most 5-star businesses. Output the city name along with the number of 5-star businesses. Include both open and closed businesses.
-- In the case of multiple cities having the same number of 5-star businesses, use the ranking function returning the lowest rank in the group and output cities with a rank smaller than or equal to 5.
-- Table: yelp_business
-- Hints
-- Expected Output
-- yelp_business


-- business_id: varchar
-- name: varchar
-- neighborhood: varchar
-- address: varchar
-- city: varchar
-- state: varchar
-- postal_code: varchar
-- latitude: float
-- longitude: float
-- stars: float
-- review_count: int
-- is_open: int
-- categories: varchar





WITH ranked_cities AS (
    SELECT
        city,
        RANK() OVER (ORDER BY COUNT(*) DESC) AS city_rank
    FROM yelp_business
    WHERE stars = 5
    GROUP BY city
)
SELECT
    city,
    COUNT(*) AS number_of_5_star_businesses
FROM yelp_business
WHERE stars = 5
GROUP BY city
HAVING city_rank <= 5
ORDER BY city_rank DESC;
