import pandas as pd
import numpy as np

benign=pd.read_csv('Editbenign2/vandal_2013_11_crs.csv')

fm=pd.read_csv('Editbenign_fm/vandal_2013_11_fm.csv')
nts=pd.read_csv('Editbenign_nts_nts/vandal_2013_11_nts.csv')
crmcount=pd.read_csv('Editbenign_crmcount/vandal_2013_11_crmcount.csv')
crncount=pd.read_csv('Editbenign_crncount/vandal_2013_11_crncount.csv')
total=pd.read_csv('Editbenign_total/vandal_2013_11_totaledit.csv')

gcrmf=benign.groupby('username1').sum().crmf
gcrms=benign.groupby('username1').sum().crms
gcrmv=benign.groupby('username1').sum().crmv
gcrnf=benign.groupby('username1').sum().crnf
gcrns=benign.groupby('username1').sum().crns
gcrnv=benign.groupby('username1').sum().crnv
gcrf_crv=benign.groupby('username1').sum().crf_crv
gntus=benign.groupby('username1').sum().ntus


benign['crmf1']=benign.username1.apply(gcrmf.get_value)
benign['crms1']=benign.username1.apply(gcrms.get_value)
benign['crmv1']=benign.username1.apply(gcrmv.get_value)
benign['crnf1']=benign.username1.apply(gcrnf.get_value)
benign['crns1']=benign.username1.apply(gcrns.get_value)
benign['crnv1']=benign.username1.apply(gcrnv.get_value)
benign['crf_crv1']=benign.username1.apply(gcrf_crv.get_value)
benign['ntus1']=benign.username1.apply(gntus.get_value)

benign=benign.drop_duplicates(subset='username1',keep='first')

del benign['pagetitle1']
del benign['pagetitle2']
del benign['meta1']
del benign['meta2']
del benign['timedifference']
del benign['counter']
del benign['commoncategories']
del benign['crmf']
del benign['crms']
del benign['crmv']
del benign['crns']
del benign['crnf']
del benign['crnv']
del benign['crf_crv']
del benign['ntus']

benign = benign.rename(columns={
    'username1': 'username1',
    'crmf1': 'crmf',
    'crms1': 'crms',
    'crmv1': 'crmv',
    'crnf1': 'crnf',
    'crns1': 'crns',
    'crnv1': 'crnv',
    'crf_crv1': 'crf_crv',
    'ntus1': 'ntus',
})

merged1 = pd.merge(benign,crmcount,how='left', left_on='username1' , right_on='username1')
merged1.crm.fillna(0,inplace=True)
merged2 = pd.merge(merged1,crncount,how='left', left_on='username1' , right_on='username1')
merged2.crn.fillna(0,inplace=True)
merged3 = pd.merge(merged2,nts,how='left', left_on='username1' , right_on='username1')
merged3.nts_nts.fillna(0,inplace=True)
merged4 = pd.merge(merged3,fm,how='left', left_on='username1' , right_on='username1')
merged4.meta1.fillna(0,inplace=True)
merged5 = pd.merge(merged4,total,how='left', left_on='username1' , right_on='username1')
merged5.totaledit.fillna(0,inplace=True)

merged5 = merged5.rename(columns={
    'username1': 'username',
    'meta1':'fm',
})
merged5['vandal']=1
merged5.to_csv('Editbenign3/vandal_2013_11.csv',index=False, encoding='utf-8')