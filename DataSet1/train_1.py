import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

asd=pd.read_csv("Editbenign4/benign_2013_1.csv")
del asd['totaledit']

x=asd.as_matrix(columns= asd.columns[1:13])
y=asd.as_matrix(columns= asd.columns[-1:])
y=np.squeeze(y);

#splitting 70 - 30
from sklearn.cross_validation import train_test_split
xt,xtt,yt,ytt=train_test_split(x,y,test_size=0.3,random_state=3)

print('logistic regression')
lr=LogisticRegression(tol=1e-4, C=1.0, random_state=0, )
lr.fit(xt,yt)
ytestoutput=lr.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ytestoutput))
print ('ROC',roc_auc_score(ytt,ytestoutput))
target_names = ['benign', 'vandal']
print(classification_report(ytt,ytestoutput, target_names=target_names))

print('naive bayes')
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(xt,yt)
ypre=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('ROC',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
target_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(xt,yt)
ypre=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
target_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")

print('knn')
from sklearn.neighbors import KNeighborsClassifier
#neigh = KNeighborsClassifier(n_neighbors=5)
neigh = KNeighborsClassifier(n_neighbors=10)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))

print('svm')
from sklearn import svm
clf = svm.SVC()
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypp))
from sklearn.metrics import classification_report
target_names = ['benign', 'vandal']
print(classification_report(ytt,ypp, target_names=target_names))

print('knn with differnt values of n')
neigh = KNeighborsClassifier(n_neighbors=6)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")
neigh = KNeighborsClassifier(n_neighbors=7)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")
neigh = KNeighborsClassifier(n_neighbors=8)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")
neigh = KNeighborsClassifier(n_neighbors=9)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print ("")
neigh = KNeighborsClassifier(n_neighbors=12)
neigh.fit(xt,yt)
ypre=neigh.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypre))
from sklearn.metrics import roc_auc_score
print ('Roc',roc_auc_score(ytt,ypre))
from sklearn.metrics import classification_report
taret_names = ['benign', 'vandal']
print(classification_report(ytt,ypre, target_names=target_names))
print("")

#random forest
names = ['crmf','crms','crmv','crnf','crns','crnv','crf_crv','ntus','crm','crn','nts_nts','fm']
print("Random Forest")
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
rf1 = RandomForestRegressor()
rf= RandomForestClassifier(n_estimators=100,random_state=0,max_depth=6)
rf.fit(xt, yt)
rf1.fit(xt, yt)
ytestoutput=rf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ytestoutput))
print ('ROC',roc_auc_score(ytt,ytestoutput))
target_names = ['benign', 'vandal']
print(classification_report(ytt,ytestoutput, target_names=target_names))
print('features sorted by their score:')
print(sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names),reverse=True))
print('features sorted by their score:')
print(sorted(zip(map(lambda x: round(x, 4), rf1.feature_importances_), names),reverse=True))