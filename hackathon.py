# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:42:36 2021

@author: Sydney
"""
import pygal
worldmap =  pygal.maps.world.World()
worldmap.title = 'Countries'
  
# adding the countries 
worldmap.add('Random Data', { 
        'aq' : 10, 
        'cd' : 30, 
        'de' : 40, 
        'eg' : 50, 
        'ga' : 45, 
        'hk' : 23, 
        'in' : 70, 
        'jp' : 54, 
        'nz' : 41, 
        'kz' : 32, 
        'us' : 66
}) 
  
# save into the file 
worldmap.render_to_file('abc.svg') 
print("Success")
