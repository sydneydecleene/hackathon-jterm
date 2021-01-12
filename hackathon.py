# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:42:36 2021

@author: Sydney
"""
# load pandas package
import pandas as pd  
import pygal

#import data
tsv_file = open("outbreakinfo_epidemiology_data_2021-01-12.tsv")
data = pd.read_csv(tsv_file, delimiter="\t")

#creating dictionary

# creating map
worldmap =  pygal.maps.world.World()
worldmap.title = 'Countries'
  
# adding the countries 

for i in range(len(data._id)):
    worldmap.add(data.name[i], [(data.location_id[i][:2].lower(),data.confirmed_rolling_14days_ago_diff[i])])
  
# save into the file 
worldmap.render_to_file('abc.svg') 
print("Success")
