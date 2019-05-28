# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:44:19 2019

@author: nrandle
"""
import re
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_May 28, 2019_10.22.csv",header=[0])
df = df.set_index(df["ResponseId"])

#print(df["Q5.1_1"])



subQuestions = ["Within Data Science", 
                "Appropriate for coverage during first course in data science", 
                "Relevant to my job", 
                "Learned in undergraduate formal education",
                "Learned through my job",
                "Learned on my own", 
                "level of mastery from first course"]

qStart = df.columns.get_loc("Q5.1_1")
qEnd = df.columns.get_loc("Q76.2")

qDF = df.iloc[:,qStart:qEnd+1]



#qDF.columns = pd.MultiIndex.from_arrays([list(qDF.iloc[0]),qDF.columns ])
print(qDF.columns)
print(qDF.iloc[0])
#Q[0-9]{2}.1_1

def removeSubQ(df,regex,charAmount):
    for i in df.columns:
        if regex.match(i):
            df.iloc[0].loc[i] = df.iloc[0].loc[i][:-charAmount] 

removeSubQ(qDF,re.compile(r"Q[0-9]{2}.1_1"),3)



print(qDF.iloc[0].loc["Q40.1_1"])







