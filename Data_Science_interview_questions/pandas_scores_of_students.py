import pandas as pd

# Sample DataFrame creation (replace this with your actual DataFrame)
data = {
    'user_id': [1, 2, 3, 4, 5],
    'grade': ['A', 'B', 'C', 'A', 'B'],
    'test_score': [78, 63, 92, 45, 88]
}

df = pd.DataFrame(data)

# Define the score buckets
buckets = [0, 50, 75, 90, 100]

# Create a new column 'score_bucket' using pd.cut
df['score_bucket'] = pd.cut(df['test_score'], bins=buckets, right=False)

# Calculate the percentage of students in each bucket
percentage_per_bucket = df['score_bucket'].value_counts(sort=False, normalize=True).reset_index()
percentage_per_bucket.columns = ['score_bucket', 'percentage']

# Calculate the cumulative percentage
percentage_per_bucket['cumulative_percentage'] = percentage_per_bucket['percentage'].cumsum()

# Display the result
print(percentage_per_bucket)
