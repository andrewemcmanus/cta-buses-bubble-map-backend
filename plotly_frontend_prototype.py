import pandas as pd
import numpy as np
import json
import csv
import plotly.graph_objects as go

df = pd.read_csv('./stop_id-board-alight-location.csv')
df.head()
# for column in csv.reader(df):
    # print(value)
# df['text'] = df['stop_id'] + df['boardings'] + df['alightings'] + df['location']
locations = df['location'].tolist()
latitudes = []
longitudes = []
boardings = []
alightings = []
for i in range(len(locations)):
    loc = locations[i]
    new = str(loc).replace("'", '"')
    object = json.loads(new)
    latitudes.append(float(object['latitude']))
    longitudes.append(float(object['longitude']))
# print(longitudes)
boards = df['boardings'].tolist()
alights = df['alightings'].tolist()
# scale = 200
for i in range(len(boards)):
    boardings.append(float(boards[i] * 0.1))
for i in range(len(alights)):
    alightings.append(float(alights[i] * 0.1))

# './chicago-community-areas.geojson'
# new GeoJSON id for locationmode
# fig update_traces?

fig = go.Figure()
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    # locationmode = 'geojson-id',
    lon = longitudes,
    lat = latitudes,
    marker = dict(
        size = boardings,
        color = "royalblue",
        line_color = 'rgb(40,40,40)',
        line_width = 0.9,
        sizemode = 'area'
    )
))
# print(geojson)
fig.update_layout(
        title_text = 'October 2012 CTA bus boardings',
        showlegend = True,
        geo = dict(
            fitbounds = 'locations',
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()
