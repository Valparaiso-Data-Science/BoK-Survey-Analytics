# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:10:17 2019

@author: nrandle
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 180)

#importing the dataframe
df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_June+19,+2019_09.54.csv",header=[0],skiprows=[2])
df = df.set_index(df["ResponseId"])

qStart = df.columns.get_loc("UserLanguage")
qEnd = df.columns.get_loc("Q77.2")
dfDemo = df.iloc[:,pd.np.r_[0:qStart, qEnd:len(df.columns)-2]]


renameColumns = {"Q77.4_1":"White"}

renameColumns = {'Q77.2':"Country", 'Q77.3':"State", 'Q77.4_1':"White", 'Q77.4_2':"Black or African American", 
                 'Q77.4_3':"American Indian or Alaska Native", 'Q77.4_4':"Asian",
                 'Q77.4_5':"Native Hawaiian or Pacific Islander", 'Q77.4_6', 'Q77.4_6_TEXT', 'Q77.5', 'Q77.6', 'Q77.6_4_TEXT', 'Q78.1', 
                 'Q78.2', 'Q78.2_5_TEXT', 'Q78.3', 'Q78.3_5_TEXT', 'Q78.4', 'Q78.5', 'Q78.5_5_TEXT',
                 'Q78.6_1', 'Q78.6_2', 'Q78.6_3', 'Q78.6_4', 'Q78.6_5', 'Q78.6_6', 'Q78.6_7', 
                 'Q78.6_8', 'Q78.6_8_TEXT', 'Q78.7', 'Q78.7_11_TEXT'}

dfDemo = dfDemo.rename(renameColumns,axis="columns")




 





