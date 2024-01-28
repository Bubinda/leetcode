# Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.

# Example:

# Input:

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]
# Output:

# def weekly_aggregation(ts) -> [
#     ['2019-01-01', '2019-01-02'], 
#     ['2019-01-08'], 
#     ['2019-02-01', '2019-02-02'],
#     ['2019-02-05'],
# ]

from datetime import datetime
from collections import defaultdict 
import pprint as pp


def read_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def weeks_from_date(starting_date, date):
    delta = read_date(date) - read_date(starting_date)
    return delta.days // 7

def group_by_weeks(ts):
    starting_date = ts[0]
    grouped = defaultdict(list)
    for date in ts:
        grouped[weeks_from_date(starting_date, date)].append(date)
    return list(grouped.values())
 
pp.pprint(group_by_weeks(ts))


# using pandas

import pandas as pd
import pprint as pp


dataframe = pd.DataFrame({'time_stamp': ts})
dataframe['time_stamp'] = pd.to_datetime(dataframe['time_stamp'])
dataframe['Week_Number'] = dataframe['time_stamp'].dt.isocalendar().week
dataframe['time_stamp'] = dataframe['time_stamp'].astype('str')
pp.pprint(dataframe.head())

output = dataframe.groupby('Week_Number')['time_stamp'].apply(list).tolist()

pp.pprint(output)
