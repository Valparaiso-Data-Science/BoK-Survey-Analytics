# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:59:07 2019

@author: nrandle
This script's goal is to clean up the survey data analysis, 
to allow for more robust analysis
"""
import re
import pandas as pd
from columns import x
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)

df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_May 29, 2019_16.08.csv",header=[0])
df = df.set_index(df["ResponseId"])


qStart = df.columns.get_loc("Q5.1_1")
qEnd = df.columns.get_loc("Q76.2")

qDF = df.iloc[:,qStart:qEnd+1]

def removeSubQ(df,regex,charAmount):
    regex = re.compile(regex)
    for i in df.columns:
        if regex.match(i):
            df.iloc[0].loc[i] = df.iloc[0].loc[i][:-charAmount] 
    
            
regex = r"Q[0-9]{1,2}.1_"

removeSubQ(qDF,regex+"1",len(" - Within data science"))
removeSubQ(qDF,regex+"2",len(" - Appropriate for coverage during first course in data science"))
removeSubQ(qDF,regex+"3",len(" - Relevant to my job"))
removeSubQ(qDF,regex+"4",len(" - Learned in undergraduate formal education"))
removeSubQ(qDF,regex+"5",len(" - Learned through my job"))
removeSubQ(qDF,regex+"6",len(" - Learned on my own"))


regex = r"Q[0-9]{1,2}.2"

prevCol = qDF.columns[0]
for i in qDF.columns:
    if re.compile(regex).match(i):
        
        qDF.iloc[0].loc[i] = prevCol
        
    prevCol = qDF.iloc[0].loc[i]
    
qDF.loc["Questions"] = qDF.columns
qDF.columns = x

subQuestions = ["Within DS", 
                "first course", 
                "Relevant to job", 
                "Learned in edu",
                "Learned in job",
                "Learned on own", 
                "first course mastery"]

#Cloud\n  Computing, cloud based services and cloud powered services design
#Use\n  Cloud Computing technologies and cloud powered services design for data  infrastructure and data handling services














