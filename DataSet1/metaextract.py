import pandas as pd
import re
pages_file = pd.read_csv("VEWS data 2/pagescopy.tsv")
pages_final = pages_file.drop_duplicates(subset='pagetitle')

pf = pages_final[['pagetitle','pagecategories']]

def check(dataframe):
    def isMetaPage(df):
        if ':' in df["pagetitle"]:
            return 1
        else:
            return 0
    dataframe["IsPageMeta"] = dataframe[["pagetitle"]].apply(isMetaPage,axis=1)
    return dataframe

pf=check(pf)

print(pf.dtypes)
pf.to_csv('pageType.csv', encoding='utf-8')