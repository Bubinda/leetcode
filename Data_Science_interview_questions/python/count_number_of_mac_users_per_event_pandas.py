# -- Count the number of user events performed by MacBookPro users.
# -- Output the result along with the event name.
# -- Sort the result based on the event count in the descending order.
# -- Table: playbook_events
# -- Hints
# -- Expected Output
# -- playbook_events

# -- Preview
# -- user_id: int
# -- occurred_at: datetime
# -- event_type: varchar
# -- event_name: varchar
# -- location: varchar
# -- device: varchar



import pandas as pd

# Assuming you have a DataFrame named 'playbook_events'
# Replace this with your actual DataFrame and column names

# Sample data
playbook_events_data = {
    'user_id': [1, 2, 3, 4, 5],
    'occurred_at': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03']),
    'event_name': ['Event1', 'Event2', 'Event1', 'Event2', 'Event3'],
    'location': ['USA', 'Canada', 'USA', 'Canada', 'Germany'],
    'device': ['MacBookPro', 'MacBookPro', 'MacBookPro', 'OtherDevice', 'MacBookPro']
}

playbook_events = pd.DataFrame(playbook_events_data)

# Filter events performed by MacBookPro users
macbookpro_events = playbook_events[playbook_events['device'] == 'MacBookPro']

# Count the number of events for each event_name
result_df = macbookpro_events.groupby('event_name').size().reset_index(name='number_of_mac_user')

# Sort the result in descending order based on the event count
result_df = result_df.sort_values(by='number_of_mac_user', ascending=False)

print(result_df)
