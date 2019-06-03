# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:59:07 2019

@author: nrandle
This script's goal is to clean up the survey data analysis, 
to allow for more robust analysis
"""
import re
import pandas as pd
import numpy as np
from columns import x
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 180)

df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_June 3, 2019_15.27.csv",header=[0])
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
    
qDF.loc["topics"] = x

subQuestions = {"1_1":"Within DS", 
                "1_2":"first course", 
                "1_3":"Relevant to job", 
                "1_4":"Learned in edu",
                "1_5":"Learned in job",
                "1_6":"Learned on own", 
                "2":"first course mastery"}

def splitRemove(s):
    s = s.split(".")
    return s[-1]


questionGroups = np.array_split(qDF.columns,72)
for i in questionGroups:
    topicname = qDF[i].iloc[-1][0]
    print(topicname)
    qDFnoTopics = qDF[i].drop(qDF[i].index[-1])
    melted = qDFnoTopics.reset_index().melt(id_vars=["ResponseId"],value_name = topicname).set_index("ResponseId")
    melted = melted.groupby(["ResponseId",melted.columns[0]]).sum()
    meltedRenamed = melted.rename(splitRemove,level = 1)
    
    if i[0] == questionGroups[0][0]:    
        output = meltedRenamed
    else:
        output = pd.merge(output, meltedRenamed,how='outer', left_index = True, right_index = True)
output = output.drop("Response ID")
output = output.rename(subQuestions,level = 1)

#Cloud\n  Computing, cloud based services and cloud powered services design
#Use\n  Cloud Computing technologies and cloud powered services design for data  infrastructure and data handling services














