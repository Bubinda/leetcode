# “To better understand the effect of the review count on the price of accommodation, categorize the number of reviews into the following groups along with the price.
#     0 reviews: NO
#     1 to 5 reviews: FEW
#     6 to 15 reviews: SOME
#     16 to 40 reviews: MANY
#     more than 40 reviews: A LOT
# Output the price and its categorization. Perform the categorization on accommodation level.“


import pandas as pd
import numpy as np

# first we need to get the data
airbnb_search_details = pd.read_csv('airbnb_search_details.csv')

# then we need to create a new column with the qualification of the number of reviews
num_reviews = airbnb_search_details['number_of_reviews']

# based on the categories of the review we will set the bins according to the corresponding ranges
condlist = [num_reviews == 0, num_reviews.between(1,5),num_reviews.between(5,15),num_reviews.between(15,40),num_reviews>40]

# the corresponding values for the bins
# we will use the same values as the ones used in the previous exercise
# NO, FEW, SOME, MANY, A LOT
choicelist = ['NO','FEW','SOME','MANY','A LOT']

# we will use the select function (take the bins and their names) to create a new column with the qualification of the number of reviews 
airbnb_search_details['reviews_qualification'] = np.select(condlist,choicelist)

# the last step is to group by the qualification of the number of reviews and get the mean of the price
#airbnb_search_details = airbnb_search_details.groupby('reviews_qualification').mean()

# we will print the result
result = airbnb_search_details[['reviews_qualification','price']]