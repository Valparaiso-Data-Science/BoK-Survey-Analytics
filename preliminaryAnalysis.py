# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:44:19 2019

@author: nrandle
"""
import re
import pandas as pd
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 240)

df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_May 28, 2019_10.22.csv",header=[0])
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

qDF.columns = pd.MultiIndex.from_arrays([list(qDF.iloc[0]),qDF.columns ])
 
qDF = qDF.drop(df.index[0])

subQuestions = ["Within DS", 
                "first course", 
                "Relevant to job", 
                "Learned in edu",
                "Learned in job",
                "Learned on own", 
                "first course mastery"]

subQHeaders = []
for i in qDF.columns.levels[1]:
    for j in range(6):
        if re.compile(r"Q[0-9]{1,2}.1_%s" % str(j+1)).match(i):
            subQHeaders.append(subQuestions[j])
    if re.compile(r"Q[0-9]{1,2}.2").match(i):
        subQHeaders.append("level of mastery from first course")
        
qDF.columns.set_levels(subQHeaders,level=1,inplace = True,verify_integrity=False)

print(qDF["Adhere\n  to the principles of the Open Data, Open Science, Open Access, use ORCID\n  based services"])





