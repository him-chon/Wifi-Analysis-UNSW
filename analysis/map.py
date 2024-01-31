import plotly.express as px
import pandas as pd

df = pd.read_csv("data/mac.csv")

color_scale = ["red", "yellow", "green"]

fig = px.scatter_mapbox(df,
                        lat="gps latitude",
                        lon="gps longitude",
                        # hover_name="Address",
                        # hover_data=["Address", "Listed"],
                        color="rssi",
                        color_continuous_scale=color_scale,
                        size="rssi+100",
                        zoom=17,
                        height=800,
                        width=1280)

fig.update_layout(showlegend=False)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()