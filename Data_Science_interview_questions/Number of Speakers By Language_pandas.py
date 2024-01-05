# -- Find the number of speakers of each language by country. Output the country, language, and the corresponding number of speakers. Output the result based on the country in ascending order.
# -- Tables: playbook_events, playbook_users
# -- Hints
# -- Expected Output


# -- playbook_events

# -- user_id: int
# -- occurred_at: datetime
# -- event_type: varchar
# -- event_name: varchar
# -- location: varchar
# -- device: varchar


# -- playbook_users

# -- user_id: int
# -- created_at: datetime
# -- company_id: int
# -- language: varchar
# -- activated_at: datetime
# -- state: varchar



import pandas as pd

# Assuming you have DataFrames named 'playbook_users' and 'playbook_events'
# Replace this with your actual DataFrames and column names

# Sample data
playbook_users_data = {
    'user_id': [1, 2, 3, 4, 5, 6],
    'location': ['USA', 'Canada', 'Canada', 'USA', 'Canada', 'Germany'],
    'language': ['English', 'French', 'German', 'English', 'French', 'German']
}

playbook_events_data = {
    'user_id': [1, 2, 3, 4, 5, 6],
    'event_name': ['Event1', 'Event2', 'Event1', 'Event2', 'Event3', 'Event1']
}

playbook_users = pd.DataFrame(playbook_users_data)
playbook_events = pd.DataFrame(playbook_events_data)

# Merge the DataFrames on the 'user_id' column
merged_df = pd.merge(playbook_users, playbook_events, on='user_id')

# Group by 'location' and 'language', then count the number of speakers
result_df = merged_df.groupby(['location', 'language']).size().reset_index(name='speaker_count')

# Sort the result in ascending order by 'location' and descending order by 'speaker_count'
result_df = result_df.sort_values(by=['location', 'speaker_count'], ascending=[True, False])

print(result_df)


