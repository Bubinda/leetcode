# “Return the total number of comments received for each user in the last 30 days. Don't output users who haven't received any comment in the defined time period. Assume today is 2020-02-10.” 



import pandas as pd

# we import the timedelta function from datetime
# to calculate the difference between two dates
from datetime import timedelta


result = fb_comments_count[(fb_comments_count['created_at'] >= pd.to_datetime('2020-02-10') - timedelta(days=30)) &
                            (fb_comments_count['created_at'] <= pd.to_datetime('2020-02-10'))].groupby('user_id')['number_of_comments'].sum().reset_index()

result = result.rename(columns={'number_of_comments_in_last_30_days': 'total_comments'})

result = result[result['total_comments'] > 0]

print(result)
