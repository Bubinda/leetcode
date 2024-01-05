# -- Find the day of the week that most people want to check-in.
# -- Output the day of the week alongside the corresponding check-incount.
# -- Table: airbnb_contacts
# -- Hints
# -- Expected Output
# -- airbnb_contacts


# -- id_guest: varchar
# -- id_host: varchar
# -- id_listing: varchar
# -- ts_contact_at: datetime
# -- ts_reply_at: datetime
# -- ts_accepted_at: datetime
# -- ts_booking_at: datetime
# -- ds_checkin: datetime
# -- ds_checkout: datetime
# -- n_guests: int
# -- n_messages: int


import pandas as pd

# Assuming you have a DataFrame named 'airbnb_contacts'
# Replace this with your actual DataFrame and column names

# Sample data
airbnb_contacts_data = {
    'id_guest': ['guest1', 'guest2', 'guest3', 'guest4', 'guest5'],
    'id_host': ['host1', 'host2', 'host3', 'host4', 'host5'],
    'ds_checkin': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02'],
    'ds_checkout': ['2023-01-02', '2023-01-03', '2023-01-02', '2023-01-04', '2023-01-03'],
    'n_guests': [2, 1, 3, 2, 1],
    'n_messages': [5, 3, 7, 2, 4]
}

airbnb_contacts = pd.DataFrame(airbnb_contacts_data)

# Convert 'ds_checkin' to datetime format
airbnb_contacts['ds_checkin'] = pd.to_datetime(airbnb_contacts['ds_checkin'])

# Filter DataFrame for non-null check-in dates
filtered_df = airbnb_contacts[airbnb_contacts['ds_checkin'].notnull()]

# Extract weekday from 'ds_checkin'
filtered_df['weekday'] = filtered_df['ds_checkin'].dt.strftime('%A')

# Group by weekday and count the number of check-ins
result_df = filtered_df.groupby('weekday').size().reset_index(name='checkin_count')

# Sort the result in descending order of check-in count
result_df = result_df.sort_values(by='checkin_count', ascending=False)

print(result_df)
