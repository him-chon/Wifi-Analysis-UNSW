import pandas as pd

df = pd.read_csv('5_GHz.csv')

df = df.groupby(['gps latitude', 'gps longitude']).agg(
    {'ssid': pd.Series.nunique}).reset_index()

print(df)

df.to_csv('5_interference_full.csv', index=False)