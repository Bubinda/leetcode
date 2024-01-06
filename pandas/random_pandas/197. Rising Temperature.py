# -- +---------------+---------+
# -- | Column Name   | Type    |
# -- +---------------+---------+
# -- | id            | int     |
# -- | recordDate    | date    |
# -- | temperature   | int     |
# -- +---------------+---------+
# -- id is the column with unique values for this table.
# -- This table contains information about the temperature on a certain day.
 

# -- Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

# -- Return the result table in any order.

# -- The result format is in the following example.

 

# -- Example 1:

# -- Input: 
# -- Weather table:
# -- +----+------------+-------------+
# -- | id | recordDate | temperature |
# -- +----+------------+-------------+
# -- | 1  | 2015-01-01 | 10          |
# -- | 2  | 2015-01-02 | 25          |
# -- | 3  | 2015-01-03 | 20          |
# -- | 4  | 2015-01-04 | 30          |
# -- +----+------------+-------------+
# -- Output: 
# -- +----+
# -- | id |
# -- +----+
# -- | 2  |
# -- | 4  |
# -- +----+
# -- Explanation: 
# -- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
# -- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).


import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    # Perform a self-join to compare each date's temperature with the previous day
    weather['recordDate_prev'] = weather['recordDate'] + pd.DateOffset(1)
    result_df = pd.merge(weather, weather, left_on='recordDate', right_on='recordDate_prev', suffixes=('', '_prev'))

    # Select rows where the temperature is higher than the previous day
    result_df = result_df[result_df['temperature'] > result_df['temperature_prev']]

    # Display the 'id' column from the result DataFrame
    output_df = result_df[['id']]

    return output_df


# more compact
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[
        (weather.temperature.diff() > 0)
      & (weather.recordDate.diff().dt.days == 1)
    ][['id']]