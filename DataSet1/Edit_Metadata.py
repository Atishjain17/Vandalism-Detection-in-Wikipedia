import pandas as pd

users_file = pd.read_csv("vews_dataset_v1.1/benign_2013_1.csv")
pageType = pd.read_csv("pageType.csv")
print(pageType)
users =users_file[['username','revtime','pagetitle']]

merged_inner = pd.merge(left=users,right=pageType, left_on='pagetitle', right_on='pagetitle')
print(merged_inner)
merged_inner.to_csv('EditMetaData.csv', encoding='utf-8')

#To seperate the categories
'''
n= pages_final.pagecategories.count()
for i in  range(10):
    s= eval(pages_final.pagecategories[i])
   # pages_file['pagecat']=s

    pages_final.set_value(i,'pagecategories',s)

#    for j in s:
 #       str = j.split(':')[1]
#pages_file.to_csv('pagesFinal.csv')
print(pages_file)
'''