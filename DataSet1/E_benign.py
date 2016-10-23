import pandas as pd
import numpy as np
from datetime import timedelta

users_file = pd.read_csv("vews_dataset_v1.1/benign_2013_2.csv")
pages_file = pd.read_csv("pageType.csv")
pages = pages_file[['pagetitle', 'IsPageMeta','pagecategories']]
users = users_file[['username', 'pagetitle', 'revtime']]
users['id'] = range(len(users))
pagesinfo_merged = pd.merge(left=users, right=pages, left_on='pagetitle', right_on='pagetitle')
users=pagesinfo_merged
users=users.sort(['id'], ascending=True)
del users['id']
users['revtime1'] = pd.to_datetime(users['revtime'])
del users['revtime']
users.index = range(0,len(users))
users1 = users.ix[1:]
users2 = users.ix[2:]
del users2['pagecategories']
del users2['IsPageMeta']

users = users.rename(columns={
    'username': 'username1',
    'pagetitle': 'pagetitle1',
    'revtime1': 'revtime1',
    'pagecategories': 'pagecategories1',
    'IsPageMeta': 'meta1',
})
users1 = users1.rename(columns={
    'username': 'username2',
    'pagetitle': 'pagetitle2',
    'revtime1': 'revtime2',
    'pagecategories': 'pagecategories2',
    'IsPageMeta': 'meta2',
})
users2 = users2.rename(columns={
    'username': 'username3',
    'pagetitle': 'pagetitle3',
    'revtime1': 'revtime3',
})
users['counter'] = range(len(users))
users1['counter'] = range(len(users1))
users2['counter'] = range(len(users2))
merged_inner = pd.merge(left=users, right=users1, left_on='counter', right_on='counter')
merged_inner1 = merged_inner[merged_inner.username1 == merged_inner.username2]
merged_inner1.index = range(0,len(merged_inner1))
merged_inner1['timedifference'] = (merged_inner1['revtime2'] - merged_inner1['revtime1'])

merged_inner1['commoncategories'] = 0
n = len(merged_inner1)
print(n)
for i in range(n):
    c1 = eval(merged_inner1.pagecategories1[i])
    c2 = eval(merged_inner1.pagecategories2[i])
    print(i)
    category1 = (c1)
    category2 = (c2)
    if(c1 != set()):
        if(c2 != set()):
            commoncat = list(set(c1).intersection(c2))
            commoncategories = len(commoncat)
            merged_inner1.ix[i,'commoncategories'] = commoncategories
        else:
            merged_inner1.ix[i,'commoncategories'] = -1

    else:
        merged_inner1.ix[i,'commoncategories']= -1

del merged_inner1['pagecategories1']
del merged_inner1['pagecategories2']
merged_inner2 = pd.merge(left=merged_inner1, right=users2, left_on='counter', right_on='counter')
merged_inner3 = merged_inner2[merged_inner2.username2 == merged_inner2.username3]
merged_inner3['timedifference1'] = (merged_inner3['revtime3'] - merged_inner3['revtime2'])

del merged_inner1['revtime1']
del merged_inner1['revtime2']
del merged_inner1['username2']
print(merged_inner1.dtypes)

merged_inner1.to_csv('Editbenign1/benign_2013_2_1.csv',index=False, encoding='utf-8')

del merged_inner3['revtime1']
del merged_inner3['revtime2']
del merged_inner3['username2']
del merged_inner3['revtime3']
del merged_inner3['pagetitle3']
del merged_inner3['username3']
del merged_inner3['meta2']
del merged_inner3['meta1']

userscrf=merged_inner3[merged_inner3.pagetitle1==merged_inner3.pagetitle2]
userscrf1=userscrf[userscrf.timedifference<timedelta(minutes=15 )]
userscrf_crv=userscrf1[userscrf1.timedifference1<timedelta(minutes=3 )]
userscrf_crv['crf_crv'] = 1

del userscrf_crv['pagetitle2']
del userscrf_crv['timedifference']
del userscrf_crv['username1']
del userscrf_crv['timedifference1']
del userscrf_crv['pagetitle1']
del userscrf_crv['commoncategories']
print(userscrf_crv.dtypes)
userscrf_crv.to_csv('Editbenign_crf_crv/benign_2013_2_1_crf_crv.csv',index=False, encoding='utf-8')

usersfm=users[['username1','meta1']]
usersfm=usersfm.drop_duplicates(subset='username1',keep='first')
print(usersfm.dtypes)
usersfm.to_csv('Editbenign_fm/benign_2013_2_1_fm.csv',index=False, encoding='utf-8')

usersmeta=merged_inner1[['counter','pagetitle1','pagetitle2','meta1','meta2','timedifference']]
usersmeta=usersmeta[usersmeta.meta1==1]
usersmeta=usersmeta[usersmeta.meta2==1]
userscrm=usersmeta[usersmeta.pagetitle1==usersmeta.pagetitle2]
del userscrm['meta2']
del userscrm['meta1']
del userscrm['pagetitle2']
del userscrm['pagetitle1']
userscrmv=userscrm[userscrm.timedifference<timedelta(minutes=3 )]
userscrmv['crmv'] = 1
del userscrmv['timedifference']
print(userscrmv.dtypes)
userscrmv.to_csv('Editbenign_crmv/benign_2013_2_1_crmv.csv',index=False, encoding='utf-8')

userscrms=userscrm[userscrm.timedifference>timedelta(minutes=15 )]
userscrms['crms'] = 1
del userscrms['timedifference']
print(userscrms.dtypes)
userscrms.to_csv('Editbenign_crms/benign_2013_2_1_crms.csv',index=False, encoding='utf-8')

userscrmf=userscrm[userscrm.timedifference<timedelta(minutes=15 )]
userscrmf=userscrmf[userscrmf.timedifference>timedelta(minutes=3 )]
userscrmf['crmf'] = 1
del userscrmf['timedifference']
print(userscrmf.dtypes)
userscrmf.to_csv('Editbenign_crmf/benign_2013_2_1_crmf.csv',index=False, encoding='utf-8')

usersnormal=merged_inner1[['counter','pagetitle1','pagetitle2','meta1','meta2','timedifference']]
usersnormal=usersnormal[usersnormal.meta1==0]
usersnormal=usersnormal[usersnormal.meta2==0]
userscrn=usersnormal[usersnormal.pagetitle1==usersnormal.pagetitle2]
del userscrn['meta2']
del userscrn['meta1']
del userscrn['pagetitle2']
del userscrn['pagetitle1']

userscrnv=userscrn[userscrn.timedifference<timedelta(minutes=3 )]
userscrnv['crnv'] = 1
del userscrnv['timedifference']
print(userscrnv.dtypes)
userscrnv.to_csv('Editbenign_crnv/benign_2013_2_1_crnv.csv',index=False, encoding='utf-8')

userscrns=userscrn[userscrn.timedifference>timedelta(minutes=15 )]
userscrns['crns'] = 1
del userscrns['timedifference']
print(userscrns.dtypes)
userscrns.to_csv('Editbenign_crns/benign_2013_2_1_crns.csv',index=False, encoding='utf-8')

userscrnf=userscrn[userscrn.timedifference<timedelta(minutes=15 )]
userscrnf=userscrnf[userscrnf.timedifference>timedelta(minutes=3 )]
userscrnf['crnf'] = 1
del userscrnf['timedifference']
print(userscrnf.dtypes)
userscrnf.to_csv('Editbenign_crnf/benign_2013_2_1_crnf.csv',index=False, encoding='utf-8')
usersnormal1=merged_inner1[['username1','counter','pagetitle1','pagetitle2','meta1','meta2']]
usersnormal1=usersnormal1[usersnormal1.meta1==0]
usersnormal1=usersnormal1[usersnormal1.meta2==0]
userscrn1=usersnormal1[usersnormal1.pagetitle1==usersnormal1.pagetitle2]

del userscrn1['pagetitle1']
del userscrn1['pagetitle2']
del userscrn1['meta1']
del userscrn1['meta2']
userscrn1 = userscrn1.rename(columns={
    'counter': 'crn',
})
userscrncount=userscrn1.groupby(['username1']).count()
userscrncount.to_csv('Editbenign_crncount/benign_2013_2_1_crncount.csv', encoding='utf-8')

usersmeta1=merged_inner1[['username1','counter','pagetitle1','pagetitle2','meta1','meta2']]
usersmeta1=usersmeta1[usersmeta1.meta1==1]
usersmeta1=usersmeta1[usersmeta1.meta2==1]
userscrm1=usersmeta1[usersmeta1.pagetitle1==usersmeta1.pagetitle2]

del userscrm1['pagetitle1']
del userscrm1['pagetitle2']
del userscrm1['meta1']
del userscrm1['meta2']
userscrm1 = userscrm1.rename(columns={
    'counter': 'crm',
})
userscrmcount=userscrm1.groupby(['username1']).count()
userscrmcount.to_csv('Editbenign_crmcount/benign_2013_2_1_crmcount.csv', encoding='utf-8')

userscrm2=merged_inner1[['username1','counter','pagetitle1','pagetitle2','meta1','meta2']]
del userscrm2['pagetitle1']
del userscrm2['pagetitle2']
del userscrm2['meta1']
del userscrm2['meta2']
userscrm2 = userscrm2.rename(columns={
    'counter': 'totaledit',
})

userscount=userscrm2.groupby(['username1']).count()
userscount.to_csv('Editbenign_total/benign_2013_2_1_totaledit.csv', encoding='utf-8')