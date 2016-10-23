import sklearn.externals.joblib as joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import json

adaboost = "Adaboost_model_save.pkl"
bnb = "BernoulliNB_model_save.pkl"
gnb = "GaussNB_model_save.pkl"
extraTree = "ExtraTreeClassifier_model_save.pkl"
knn = "KNN_model_save.pkl"
lr = "lr_model_save.pkl"
rf = "RandomForest_model_save.pkl"
svm = "SVM_model_save.pkl"
gbt = "GradientBoost_model_save.pkl"

adaClf = joblib.load(adaboost)
bnbClf = joblib.load(bnb)
gnbClf = joblib.load(gnb)
extraTreeClf = joblib.load(extraTree)
knnClf = joblib.load(knn)
lrClf = joblib.load(lr)
rfClf = joblib.load(rf)
svmClf = joblib.load(svm)
gbtClf = joblib.load(gbt)

testdata = pd.read_csv("testData.csv", header=0)
testdata = testdata.values

X = testdata[2:-1]
y = testdata[-1]

adaY = adaClf.predict(X)
bnbY = bnbClf.predict(X)
gnbY = gnbClf.predict(X)
etY = extraTreeClf.predict(X)
knnY = knnClf.predict(X)
lrY = lrClf.predict(X)
rfY = rfClf.predict(X)
svmY = svmClf.predict(X)
gbtY = gbtClf.predict(X)

adaScore = accuracy_score(y, adaY)
bnbScore = accuracy_score(y, bnbY)
gnbScore = accuracy_score(y, gnbY)
etScore = accuracy_score(y, etY)
knnScore = accuracy_score(y, knnY)
lrScore = accuracy_score(y, lrY)
rfScore = accuracy_score(y, rfY)
svmScore = accuracy_score(y, svmY)
gbtScore = accuracy_score(y, gbtY)

result = { "adaboost" : adaScore,
           "bnb" : bnbScore,
           "gnb" : gnbScore,
           "et" : etScore,
           "knn" : knnScore,
           "lr" : lrScore,
           "rf" : rfScore,
           "svm" : svmScore,
           "gbt" : gbtScore }

print(json.dumps(result))
input()