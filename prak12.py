# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:24:09 2023

@author: Huawei
"""

import pandas as pd

df = pd.read_csv('Negara.csv', index_col = 0)
mean = df.groupby(['Benua']).mean(numeric_only=True)
deviation = df.groupby(['Benua']).std(numeric_only=True)

print("Berikut Data Framenya: ")
print(df, "\n")

print("Berikut Hasil Mean")
print(mean, "\n")

print("Standart Deviation: ")
print(deviation, "\n")