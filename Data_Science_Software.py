# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import eurostat

Data_List = eurostat.get_toc()
df = pd.DataFrame(Data_List)
 


       
