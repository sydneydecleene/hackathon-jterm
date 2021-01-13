# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:42:36 2021
@author: Sydney
"""

# load pandas package
import pandas as pd  
import pygal
from pygal.style import Style

#import data
file = input('Please cases data to visualize: ')
tsv_file = open(file)
data = pd.read_csv(tsv_file, delimiter="\t")


# creating map
custom_style = Style(opacity='1', colors=('#75ABD0', '#ABD6E7', '#DCF1EC','#FAF8C1','#FEDD90','#FCAC64','#F16E43','#D4322C','#A50026'))
worldmap =  pygal.maps.world.World(style=custom_style)
worldmap.title = 'Countries'

low_1 = {}
low_2 = {}
low_3 = {}
high_1 = {}
high_2 = {}
high_3 = {}
high_4 = {}
high_5 = {}
high_6 = {}
# adding the countries to specific range
for i in range(len(data._id)):
    if data.confirmed_rolling_14days_ago_diff[i] < -81156:
        low_1[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < -8951:
        low_2[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < -1810:
        low_3[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < 2157:
        high_1[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < 6125:
        high_2[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < 14853:
        high_3[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < 28657:
        high_4[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] < 92612:
        high_5[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]
    else:
        high_6[data.location_id[i][:2].lower()] = data.confirmed_rolling_14days_ago_diff[i]


worldmap.add('1',low_1)
worldmap.add('2',low_2)
worldmap.add('3',low_3)
worldmap.add('h1',high_1)
worldmap.add('h2',high_2)
worldmap.add('h3',high_3)
worldmap.add('h4',high_4)
worldmap.add('h5',high_5)
worldmap.add('h6',high_6)

# save into the file 
worldmap.render_to_file('abc.svg') 
print("Success")