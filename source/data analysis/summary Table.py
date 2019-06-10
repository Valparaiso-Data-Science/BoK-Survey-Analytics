# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:26:08 2019

@author: nrandle
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 180)

import seaborn as sns

df = pd.read_pickle("../../data/courses.pkl")

#this grabs the 'within ds' values, removes the 0s for easy counting, counts all the collumns, 
#transposes its from columns to rows (so each topic is a row), and turns the nans (which means the "agree"/"disagree" didnt show up) to 0s
agreeCount = df.xs("Within DS",level=1).replace(0,np.NaN).apply(pd.Series.value_counts).transpose().fillna(0)


agreeCount["n"] = agreeCount["Agree/Yes"] + agreeCount["Disagree/No"] 
agreeCount["Agree/Yes"] = agreeCount["Agree/Yes"]/(agreeCount["Agree/Yes"]+agreeCount["Disagree/No"])
agreeCount["Disagree/No"] = 1-agreeCount["Agree/Yes"]



plt.figure(figsize=(6,40))
sns.set(font_scale=2)
x = sns.heatmap(agreeCount.sort_values(["Agree/Yes","Disagree/No"],ascending=False),
                annot=True,xticklabels=True,cbar=False,
                cmap=sns.color_palette("YlOrRd"),
                vmin = 0, vmax = 1,center=.5)


x = x.get_figure()
x.savefig("output.png",dpi=250,bbox_inches="tight")

"""
summary table goal

        % agree    % disagree     count
topic 1
topic 2
...
topic n



"""