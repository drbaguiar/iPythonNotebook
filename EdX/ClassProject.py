# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:50:43 2015

@author: ldierker
"""
import pandas
import numpy
# any additional libraries would be imported here

data = pandas.read_csv('D:/Data/EdX/gapminder.csv')

print (len(data)) #number of observations (rows)
print (len(data.columns)) # number of variables (columns)
