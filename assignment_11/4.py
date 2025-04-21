import pandas as pd
import numpy as np
df = pd.DataFrame({
    'day': range(10),
    'John': [True, False, True, False, True, True, False, True, True, False],
    'Judy': [False, True, True, False, False, True, True, True, False, True]
})
df['party'] = (df['John'] & df['Judy'])
days_til_party = [np.nan] * len(df)
party_index = None
for i in range(len(df) - 1, -1, -1):
    if df.loc[i, 'party']:
        days_til_party[i] = 0
        party_index = i 
    elif party_index is not None:
        days_til_party[i] = party_index - i
    else:
        days_til_party[i] = np.nan

df['days_til_party'] = days_til_party
print(df)
