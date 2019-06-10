# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:26:08 2019

@author: nrandle
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 180)


df = pd.read_pickle("../../data/courses.pkl")

subQuestions = ["Within DS", 
                "first course", 
                "Relevant to job", 
                "Learned in edu",
                "Learned in job",
                "Learned on own"]
output = pd.DataFrame()

#for each subheading
for q in subQuestions:
    print("starting: " + q)
    
    #this grabs df, removes the 0s for easy counting, counts all the collumns, 
    #transposes its from columns to rows (so each topic is a row), and turns the nans (which means the "agree"/"disagree" didnt show up) to 0s

    agreeCount = df.xs(q,level=1).replace(0,np.NaN).apply(pd.Series.value_counts).transpose().fillna(0)
    
    #create a count 
    agreeCount["Agree/Yes"] = agreeCount["Agree/Yes"]/(agreeCount["Agree/Yes"]+agreeCount["Disagree/No"])
    agreeCount = agreeCount.drop("Disagree/No",axis=1)
    agreeCount.columns = [q]
    output = pd.merge(output, agreeCount,how='outer', left_index = True, right_index = True)
    
    
plt.figure(figsize=(20,40))
sns.set(font_scale=2)

x = sns.heatmap(output.sort_values(list(output.columns),ascending=False),
                annot=True, xticklabels=True, cbar=True,
                cmap=sns.color_palette("PuOr", 20),
                vmin = 0, vmax = 1,center=.5
                )
print("plotting: " + q)
plt.title("Topic %s" % q)
x = x.get_figure()
x.savefig("output2.png",dpi=200,bbox_inches="tight")


"""
summary table goal

        % agree    % disagree     count
topic 1
topic 2
...
topic n



"""