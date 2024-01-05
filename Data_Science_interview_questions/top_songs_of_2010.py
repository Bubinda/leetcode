# “What were the top 10 ranked songs in 2010? Output the rank, group name, and song name but do not show the same song twice. Sort the result based on the year_rank in ascending order.”


import pandas as pd
import numpy as np

#get all the songs from the year 2010 and also only filter out the ones where the rank is in the range of 1 to 10
conditions = billboard_top_100_year_end[(billboard_top_100_year_end['year'] == 2010) & (billboard_top_100_year_end['year_rank'].between(1,10))]

# to get a clear set also include to filter out the duplicates if included
result = conditions[['year_rank','group_name','song_name']].drop_duplicates()