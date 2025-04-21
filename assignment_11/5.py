import pandas as pd
# import numpy as np
data = {
    'date': ['2023-01-15', '2023-01-20', '2023-01-28', 
             '2023-02-05', '2023-02-15', '2023-02-20',
             '2023-03-01', '2023-03-10', '2023-03-15', '2023-03-20'],
    'artist': ['The Band', 'The Band', 'Rockers', 
               'The Band', 'Rockers', 'The Band',
               'Rockers', 'Rockers', 'The Band', 'Rockers'],
    'venue': ['Stadium A', 'Club X', 'Stadium A', 
              'Club X', 'Stadium A', 'Stadium A',
              'Club X', 'Stadium A', 'Club X', 'Club X']
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')
concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

unique_artists = df['artist'].unique()
unique_venues = df['venue'].unique()

index = pd.MultiIndex.from_product([unique_artists, unique_venues], names=['artist', 'venue'])
result = concert_counts.pivot(index='year_month', columns=['artist', 'venue'], values='count')
# print(result)
result = result.reindex(columns=index)
print(result)
