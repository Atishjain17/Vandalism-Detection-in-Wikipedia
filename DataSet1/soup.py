from urllib.request import urlopen, HTTPError
from urllib import parse
from bs4 import BeautifulSoup
import pandas as pd

df2 = pd.read_csv("hopn/benign_2013_8hopn1.csv", encoding='utf-8')
df2['hop']= ""
n = len(df2.pagetitle1)

def getdegree(url):
    try:
        print(url)
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        degree = bsObj.h1
    except AttributeError as e:
        return None
    return degree

print(n)
for i in range(n):
    #Convert non-ascii to percent encoded form- a1,a2
    a1 = parse.quote(df2.pagetitle1[i]).replace("%20", "+")
    a2 = parse.quote(df2.pagetitle2[i]).replace("%20", "+")

    url = "http://beta.degreesofwikipedia.com/?a1="+ a1 +"+&linktype=1&a2=" + a2 + "&skips=&submit=1458023344&currentlang=en"
    degree = getdegree(url)
    if(degree == None):
        df2.hop[i] = degree
    else:
        df2.hop[i] = str(degree).split("<br/>")[1].split(" ")[0]
    print(df2.counter[i],"\t", df2.hop[i])
    print(i)
df2.to_csv('benign_2013_8_hopn1.csv',index=False, encoding='utf-8')