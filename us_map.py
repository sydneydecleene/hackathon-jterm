# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:50:15 2021

@author: Mariana
"""
import plotly
import plotly.graph_objects as go

import pandas as pd
data = pd.read_csv('us_outbreakinfo_epidemiology_data_2021-01-13.tsv', delimiter="\t")
codes = []
for i in range(len(data._id)):
    codes.append(data.location_id[i][-2:])

fig = go.Figure(data=go.Choropleth(
    locations=codes, # Spatial coordinates
    z = data.confirmed_rolling_14days_ago_diff, # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    ))

fig.update_layout(
    title_text = '2 week change in cases/day',
    geo_scope='usa', # limite map scope to USA
    )

fig.show()

plotly.offline.plot(fig, filename='our_data.html')