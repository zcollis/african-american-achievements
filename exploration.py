#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:53:28 2021

@author: zhaire
"""

#data collection through kaggle.com
#data loading and exploration

import pandas as pd
firsts_path = 'firsts.csv'
science_path = 'science.csv'

firsts_data = pd.read_csv('firsts.csv')
science_data = pd.read_csv('science.csv')

firsts_data.describe()
science_data.describe()

print(firsts_data.head())
print(science_data.head())

