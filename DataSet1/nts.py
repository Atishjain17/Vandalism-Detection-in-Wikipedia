import pandas as pd
import numpy as np

benignhop= pd.read_csv("hopn1/benign_2013_2_hopn.csv")
vandalhop= pd.read_csv("hopn1/vandal_2013_2_hopn.csv")

del benignhop['pagetitle1']
del benignhop['pagetitle2']
del benignhop['counter']
del benignhop['hop']
del vandalhop['pagetitle1']
del vandalhop['pagetitle2']
del vandalhop['counter']
del vandalhop['hop']

groupu=benignhop.groupby('username1').sum().nhop
benignhop['nts_nts']=benignhop.username1.apply(groupu.get_value)
benignhop=benignhop.drop_duplicates(subset='username1',keep='first')
n=len(benignhop)
benignhop.index = range(0,n)
for i in range(n):
    if(benignhop.nts_nts[i]>0):
        benignhop.nts_nts[i]=benignhop.nts_nts[i]-1
print(benignhop)
del benignhop['nhop']

groupu1=vandalhop.groupby('username1').sum().nhop
vandalhop['nts_nts']=vandalhop.username1.apply(groupu1.get_value)
vandalhop=vandalhop.drop_duplicates(subset='username1',keep='first')
n=len(vandalhop)
vandalhop.index = range(0,n)
for i in range(n):
    if(vandalhop.nts_nts[i]>0):
        vandalhop.nts_nts[i]=vandalhop.nts_nts[i]-1
print(vandalhop)
del vandalhop['nhop']

benignhop.to_csv('Editbenign_nts_nts/benign_2013_2_1_nts.csv',index=False, encoding='utf-8')
vandalhop.to_csv('Editbenign_nts_nts/vandal_2013_2_1_nts.csv',index=False, encoding='utf-8')
