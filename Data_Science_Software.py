# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:02:07 2021

@author: las_v
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data = pd.read_csv("species.csv")


# Data Visualization 

# Bar Graph
Search = 'Park Name'
x = Data[Data[Search]== Name]
plt.bar (x,y)
plt.rcParams["figure.figsize"]=10,10
plt.grid()
plt.xlabel("x")   
plt.ylabel("y")   
plt.title('')

       
