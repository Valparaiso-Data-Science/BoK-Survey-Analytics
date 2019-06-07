# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:26:08 2019

@author: nrandle
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 180)

import seaborn as sns

df = pd.read_pickle("../../data/courses.pkl")
print(df.count(axis="columns"))


"""
summary table goal

        % agree    % disagree     count
topic 1
topic 2
...
topic n



"""