import plotly.express as px
import pandas as pd

df = pd.read_csv("data/uniwide.csv")

fig = px.scatter_geo(df,
                     lat="gps latitude",
                     lon="gps longitude",
                     hover_name="rssi")

fig.update_layout(title = 'World map', title_x=0.5)
fig.show()