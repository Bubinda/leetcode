import pandas as pd

data = pd.DataFrame()
data_grade_over_90 = data[(data['grade'] > 90)] 
data_color_filter = data_grade_over_90[(data_grade_over_90['fav_color'] == 'green') | (data_grade_over_90['color'] == 'red')]
print(data_color_filter)

#in one line

df = pd.DataFrame()

filtered_df = df[(df['favorite_color'] == 'green') | (df['favorite_color'] == 'red') & (df['grade'] > 90)]



#or more compact

filtered_df = df[(df['favorite_color'].isin(['green', 'red'])) & (df['grade'] > 90)]
