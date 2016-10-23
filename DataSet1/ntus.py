import pandas as pd
import numpy as np

benignhopnu= pd.read_csv("hopnu1/benign_2013_2_hopnu.csv")
vandalhopnu= pd.read_csv("hopnu1/vandal_2013_2_hopnu.csv")
benignhopnu['ntus']= 0
n=len(benignhopnu)
for i in range(n):
    if(benignhopnu.hop[i]>=0):
        if(benignhopnu.hop[i]<4):
            benignhopnu.ntus[i]=1

vandalhopnu['ntus']= 0
n1=len(vandalhopnu)
for j in range(n1):
    if(vandalhopnu.hop[j]>=0):
        if(vandalhopnu.hop[j]<4):
            vandalhopnu.ntus[j]=1
print(benignhopnu)
print(vandalhopnu)

benignhopnu.to_csv('Editbenign_ntus/benign_2013_2_1_ntus.csv',index=False, encoding='utf-8')
vandalhopnu.to_csv('Editbenign_ntus/vandal_2013_2_1_ntus.csv',index=False, encoding='utf-8')