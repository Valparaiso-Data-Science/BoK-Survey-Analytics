# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:44:19 2019

@author: nrandle
"""
import re
import pandas as pd
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

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
#print(qDF.columns)
#print(qDF.iloc[0])
#Q[0-9]{2}.1_1

def removeSubQ(df,regex,charAmount):
    regex = re.compile(regex)
    for i in df.columns:
        if regex.match(i):
            df.iloc[0].loc[i] = df.iloc[0].loc[i][:-charAmount] 
            
            
regex = r"Q[0-9]{2}.1_"
removeSubQ(qDF,regex+"1",len(" - Within data science"))
removeSubQ(qDF,regex+"2",len(" - Appropriate for coverage during first course in data science"))
removeSubQ(qDF,regex+"3",len(" - Relevant to my job"))
removeSubQ(qDF,regex+"4",len(" - Learned in undergraduate formal education"))
removeSubQ(qDF,regex+"5",len(" - Learned through my job"))
removeSubQ(qDF,regex+"6",len(" - Learned on my own"))

for i in list(qDF.iloc[0]):
    print(i)



regex = r"Q[0-9]{2}.2"

prevCol = qDF.columns[0]
for i in qDF.columns:
    if re.compile(regex).match(i):
        qDF.iloc[0].loc[i] = prevCol
    prevCol = qDF.iloc[0].loc[i]
   
#print(qDF.iloc[0].loc["Q20.1_1"])


#def addSubQ(df,regex,replacement):
    



qDF.columns = pd.MultiIndex.from_arrays([list(qDF.iloc[0]),qDF.columns ])
 
qDF = qDF.drop(df.index[0])
#print(qDF.columns)

#print(qDF.iloc[:,0:1])






