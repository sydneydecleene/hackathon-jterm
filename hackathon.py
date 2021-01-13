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
tsv_file = open("outbreakinfo_epidemiology_data_2021-01-12.tsv")
data = pd.read_csv(tsv_file, delimiter="\t")


# creating map
custom_style = Style(opacity='1', colors=('#75ABD0', '#ABD6E7', '#DCF1EC','#FAF8C1','#FEDD90','#FCAC64','#F16E43','#D4322C','#A50026'))
worldmap =  pygal.maps.world.World(style=custom_style)
worldmap.title = 'Countries'
col = data.name
code = {}
from pycountry_convert import  country_name_to_country_alpha2
for i in range(len(data.name)):
    try:
        code[i] = country_name_to_country_alpha2(col[i])
    except:  "Invalid Country Name: "
# adding the countries 
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
for i in range(len(code)):
    if data.confirmed_rolling_14days_ago_diff[i] <=-80362:
        low_1[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] <= -8157:
        low_2[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] <= -1000:
        low_3[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
    elif data.confirmed_rolling_14days_ago_diff[i] <= 1365:
        try: 
            high_1[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
        except: "KeyError: "
    elif data.confirmed_rolling_14days_ago_diff[i] <= 6125:
        try:
            high_2[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
        except: "KeyError: "
    elif data.confirmed_rolling_14days_ago_diff[i] <= 14060:
        try:
            high_3[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
        except: "KeyError: "
    elif data.confirmed_rolling_14days_ago_diff[i] <= 36200:
        try:
            high_4[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
        except: "KeyError: "
    elif data.confirmed_rolling_14days_ago_diff[i] <= 91820:
        try: 
            high_5[code[i]] = data.confirmed_rolling_14days_ago_diff[i]
        except: "KeyError: "
    else:
        high_6[code[i]] = data.confirmed_rolling_14days_ago_diff[i]


worldmap.add('1',low_1)
worldmap.add('2',low_2)
worldmap.add('3',low_3)
worldmap.add('h1',high_1)
worldmap.add('h2',high_2)
worldmap.add('h3',high_3)
worldmap.add('h4',high_4)
worldmap.add('h5',high_5)
worldmap.add('h6',high_6)


for i in range(len(data._id)):
    worldmap.add(data.name[i], [(data.location_id[i][:2].lower(),data.confirmed_rolling_14days_ago_diff[i])])

# save into the file 
worldmap.render_to_file('abc.svg') 
