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

#importing the dataframe
df = pd.read_csv("file:///H:/GitHub/BoK-Survey-Analytics/data/TRIPODS-X_June+10,+2019_12.20.csv",header=[0],skiprows=[2])
df = df.set_index(df["ResponseId"])

#finding the start and end of the questions
qStart = df.columns.get_loc("Q5.1_1")
qEnd = df.columns.get_loc("Q76.2")
qDF = df.iloc[:,qStart:qEnd+1]

#this function removes the amount of characters from a regex matched string in a df
def removeSubQ(df,regex,charAmount):
    regex = re.compile(regex)
    for i in df.columns:
        if regex.match(i):
            df.iloc[0].loc[i] = df.iloc[0].loc[i][:-charAmount] 
    
#regex for Q01.1_1 pattern 
regex = r"Q[0-9]{1,2}.1_"

#removeing the sub questions from the columns in the working dataframe
#note that there is no asignment because I dont understand mutability and scope
removeSubQ(qDF,regex+"1",len(" - Within data science"))
removeSubQ(qDF,regex+"2",len(" - Appropriate for coverage during first course in data science"))
removeSubQ(qDF,regex+"3",len(" - Relevant to my job"))
removeSubQ(qDF,regex+"4",len(" - Learned in undergraduate formal education"))
removeSubQ(qDF,regex+"5",len(" - Learned through my job"))
removeSubQ(qDF,regex+"6",len(" - Learned on my own"))

#copying over the names of the topics onto the first course mastery quesition due to redundency
regex = r"Q[0-9]{1,2}.2"
prevCol = qDF.columns[0]
for i in qDF.columns:
    if re.compile(regex).match(i): 
        qDF.iloc[0].loc[i] = prevCol 
    prevCol = qDF.iloc[0].loc[i]

#x is a list of the columns, but renamed to be shorter. This is more for testing, but probably won't change
qDF.loc["topics"] = x



#inputs a string, outputs a split string
def splitRemove(s):
    s = s.split(".")
    return s[-1]

#this begins the block of transforming the data into a good format
    #It can be improved by a bit, due to the specificity of the code on the number of 
    #questions. BUT thats easily fixable, and I just don't want to work that out
    #If bugs arrive where everything starts messing up, look here

#this splits the array into the number of questions (this is the bad part)
questionGroups = np.array_split(qDF.columns,72)

print("Begin topic loading \n")

#for each question group, 
    #melt the questions
    #group the melted questions by the response ID and then the topic
    #rename the questions in level one of the heirarchy to the subQuestion IDs
    #if its the first df, create a output one
    #otherwise merge the output df with the new topic
for i in questionGroups:
    topicname = qDF[i].loc["topics"][0]
    print(topicname)
    qDFnoTopics = qDF[i].drop(qDF[i].index[-1])
    melted = qDFnoTopics.reset_index().melt(id_vars=["ResponseId"],value_name = topicname).set_index("ResponseId")
    melted = melted.groupby(["ResponseId",melted.columns[0]]).sum()
    meltedRenamed = melted.rename(splitRemove,level = 1)
    
    if i[0] == questionGroups[0][0]:    
        output = meltedRenamed
    else:
        output = pd.merge(output, meltedRenamed,how='outer', left_index = True, right_index = True)
  
#a reference for the sub questions to their respective numbers
subQuestions = {"1_1":"Within DS", 
                "1_2":"first course", 
                "1_3":"Relevant to job", 
                "1_4":"Learned in edu",
                "1_5":"Learned in job",
                "1_6":"Learned on own", 
                "2":"first course mastery"}

#lastly drop the response ID row, which now contains garbage from the question data
output = output.drop("Response ID")
#and then rename the subQuestion ID's with the actual questions
output = output.rename(subQuestions,level = 1)


output.to_pickle("../../data/courses.pkl")






