# “You are given a table containing assignment scores of students in a class. Write a query that identifies the largest difference in total score of all assignments. Output just the difference in total score between the two students.”


import pandas as pd
import numpy as np
# sum up all the scores of each student for all the assignments as new column "total scores"
box_scores['total_score'] = box_scores['assignment1']+box_scores['assignment2']+box_scores['assignment3']

# get the max and the min and subtract them to get the largest difference in total assignment scores
box_scores['total_score'].max() - box_scores['total_score'].min()




