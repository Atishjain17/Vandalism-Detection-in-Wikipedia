from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn import svm
from sklearn import metrics
import numpy as np
import pandas as pd


asd=pd.read_csv("Editbenign5/13_y1.csv")
del asd['totaledit']

x=asd.as_matrix(columns= asd.columns[1:13])
y=asd.as_matrix(columns= asd.columns[-1:])
y=np.squeeze(y);
from sklearn.cross_validation import train_test_split
xt,xtt,yt,ytt=train_test_split(x,y,test_size=0.3,random_state=3,)

''''
    param_grid = {'kernel': ['rbf', 'linear'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]}

    clf = GridSearchCV(svm.SVC(), param_grid , scoring="accuracy", verbose=3,n_jobs=4,)
    clf.fit(x,y)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
'''''
print(1)
clf = svm.SVC(kernel='rbf',gamma= 1e-3, C=1)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(2)
clf = svm.SVC(kernel='rbf',gamma= 1e-3, C=10)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(3)
clf = svm.SVC(kernel='rbf',gamma= 1e-3, C=100)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(4)
clf = svm.SVC(kernel='rbf',gamma= 1e-3, C=1000)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(5)
clf = svm.SVC(kernel='rbf',gamma= 1e-4, C=1)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(6)
clf = svm.SVC(kernel='rbf',gamma= 1e-4, C=10)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(7)
clf = svm.SVC(kernel='rbf',gamma= 1e-4, C=100)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(8)
clf = svm.SVC(kernel='rbf',gamma= 1e-4, C=1000)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(9)
clf = svm.SVC(kernel='linear',gamma= 1e-3, C=1)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(10)
clf = svm.SVC(kernel='linear',gamma= 1e-3, C=10)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(11)
clf = svm.SVC(kernel='linear',gamma= 1e-3, C=100)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(12)
clf = svm.SVC(kernel='linear',gamma= 1e-3, C=1000)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(13)
clf = svm.SVC(kernel='linear',gamma= 1e-4, C=1)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(14)
clf = svm.SVC(kernel='linear',gamma= 1e-4, C=10)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(15)
clf = svm.SVC(kernel='linear',gamma= 1e-4, C=100)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

print(16)
clf = svm.SVC(kernel='linear',gamma= 1e-4, C=1000)
clf.fit(xt, yt)
ypp=clf.predict(xtt)
print ('Accuracy',metrics.accuracy_score(ytt,ypp))

''''
print('y')
print('1-Accuracy 0.791451854316, 2-Accuracy 0.819557625146, 3-Accuracy 0.824380508897, 4-Accuracy 0.81756194911,')
print('5-Accuracy 0.777482122069, 6-Accuracy 0.792782305006, 7-Accuracy 0.826376184933, 8-Accuracy 0.829369698986')
print('')
print('')

print('y1')
print('1-Accuracy 0.793114917678, 2-Accuracy 0.817728255447, 3-Accuracy 0.824546815234, 4-Accuracy 0.829536005322')
print('5-Accuracy 0.784799600865, 6-Accuracy 0.793114917678, 7-Accuracy 0.818726093464, 8-Accuracy 0.818726093464')
print('9-Accuracy 0.818726093464, 10-Accuracy 0.818726093464, 11-Accuracy 0.818726093464, 12-Accuracy 0.818726093464')
print('13-Accuracy 0.818726093464, 14-Accuracy 0.818726093464, 15-Accuracy 0.818726093464, 16-Accuracy 0.818726093464')
'''''