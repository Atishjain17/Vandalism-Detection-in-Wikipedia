import pandas as pd
import numpy as np
from datetime import timedelta

pages_file = pd.read_csv("Editbenign1/benign_2013_12.csv")
pages = pages_file[['username1','pagetitle1', 'pagetitle2', 'counter', 'timedifference','commoncategories']]

pages['timedifference'] = pd.to_timedelta(pages['timedifference'])

print(pages.dtypes)

pages=pages.drop_duplicates(['username1','pagetitle2'],keep='first')

pages = pages[pages.timedifference > timedelta(minutes=15)]
#print(pages.head(100))
pages.index = range(0, len(pages))
print(len(pages))
pages1 = pages[pages.commoncategories == -1]
pages1.index = range(0, len(pages1))
print(len(pages1))
del pages1['timedifference']
del pages1['commoncategories']

pages2 = pages[pages.commoncategories != -1]
pages2.index = range(0, len(pages2))
print(len(pages2))
del pages2['timedifference']
del pages2['commoncategories']

pages1.to_csv('hopnu/benign_2013_12hopnu.csv',index=False, encoding='utf-8')
pages2.to_csv('hopn/benign_2013_12hopn.csv',index=False, encoding='utf-8')
