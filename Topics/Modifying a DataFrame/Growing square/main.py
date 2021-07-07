import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

df['c'] = [3, 6]
df = df.append({'a': 7, 'b': 8, 'c': 9}, ignore_index=True)
