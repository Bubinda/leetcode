# -- Find the top 5 cities with the most 5-star businesses. Output the city name along with the number of 5-star businesses. Include both open and closed businesses.
# -- In the case of multiple cities having the same number of 5-star businesses, use the ranking function returning the lowest rank in the group and output cities with a rank smaller than or equal to 5.
# -- Table: yelp_business
# -- Hints
# -- Expected Output
# -- yelp_business


# -- business_id: varchar
# -- name: varchar
# -- neighborhood: varchar
# -- address: varchar
# -- city: varchar
# -- state: varchar
# -- postal_code: varchar
# -- latitude: float
# -- longitude: float
# -- stars: float
# -- review_count: int
# -- is_open: int
# -- categories: varchar



import pandas as pd

# Assuming you have a DataFrame named 'yelp_business'
# Replace this with your actual DataFrame and column names

# Sample data
yelp_business_data = {
    'business_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Business1', 'Business2', 'Business3', 'Business4', 'Business5', 'Business6', 'Business7', 'Business8'],
    'city': ['City1', 'City2', 'City1', 'City3', 'City2', 'City1', 'City3', 'City2'],
    'stars': [5, 5, 5, 4, 5, 4, 5, 5],
    'is_open': [1, 0, 1, 1, 1, 0, 1, 1]
}

yelp_business = pd.DataFrame(yelp_business_data)

# Filter DataFrame for 5-star businesses
five_star_businesses = yelp_business[yelp_business['stars'] == 5]

# Group by city and count the number of 5-star businesses
city_counts = five_star_businesses.groupby('city').size().reset_index(name='number_of_5_star_businesses')

# Rank the cities based on the number of 5-star businesses
city_counts['city_rank'] = city_counts['number_of_5_star_businesses'].rank(ascending=False, method='min')

# Select the top 5 cities
top_cities = city_counts[city_counts['city_rank'] <= 5].sort_values(by='city_rank', ascending=True)

print(top_cities)


