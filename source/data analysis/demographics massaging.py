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
df = pd.read_csv("file:///C:/Users/nrandle/Documents/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_June+28,+2019_11.49.csv",
                 header=[0],skiprows=[2])
df = df.set_index(df["ResponseId"])

#setting up only the demographics data from the data frame
qStart = df.columns.get_loc("UserLanguage")
qEnd = df.columns.get_loc("Q77.2")
dfDemo = df.iloc[:,pd.np.r_[0:qStart, qEnd:len(df.columns)-2]]

#renaming dataframe columns in order to make for easier encoding
renameColumns = {'Q77.2':"Country", 'Q77.3':"State", 'Q77.4_1':"White", 'Q77.4_2':"Black or African American", 
                 'Q77.4_3':"American Indian or Alaska Native", 'Q77.4_4':"Asian",
                 'Q77.4_5':"Native Hawaiian or Pacific Islander", 
                 'Q77.4_6':"Other Race", 'Q77.4_6_TEXT':"Other Race Text", 
                 'Q77.5':"Spanish, Hispanic, or Latino", 'Q77.6':"Pronoun", 
                 'Q77.6_4_TEXT':"Pronoun Other", 
                 'Q78.1':"Primary Role", 'Q78.2':"Area of Firm", 'Q78.2_5_TEXT':"Area of Firm other Text", 
                 'Q78.3':"Position in Firm", 'Q78.3_5_TEXT':"Position in firm Other text",
                 'Q78.4':"Years in Data Science",
                 'Q78.5':"Academic position", 'Q78.5_5_TEXT':"Academic Position Other text",
                 'Q78.6_1':"Math Dept", 'Q78.6_2':'Computer Science Dept', 'Q78.6_3':"Statistics Dept", 
                 'Q78.6_4':"Data Science Dept", 'Q78.6_5':"Business Dept", 'Q78.6_6':"Engineering Dept",
                 'Q78.6_7':"Other STEM Dept", 
                 'Q78.6_8':"Other Dept", 'Q78.6_8_TEXT':"Other Dept Text", 
                 'Q78.7':"School Classification", 'Q78.7_11_TEXT':"School Clasification Other"}
dfDemo = dfDemo.rename(renameColumns,axis="columns")

#removing useless column
dfDemo = dfDemo.drop(["Response ID","R_2ZDdGpzk73iWPXi"])


pd.to_pickle(dfDemo,"../../data/dfDemo.pkl")





