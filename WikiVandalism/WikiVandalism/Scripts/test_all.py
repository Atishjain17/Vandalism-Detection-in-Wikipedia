from sklearn.externals import joblib

adaboost = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/Adaboost_model_save.pkl"
bnb = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/BernoulliNB_model_save.pkl"
gnb = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/GaussNB_model_save.pkl"
extraTree = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/ExtraTreeClassifier_model_save.pkl"
knn = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/KNN_model_save.pkl"
lr = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/lr_model_save.pkl"
rf = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/RandomForest_model_save.pkl"
svm = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/SVM_model_save.pkl"
gbt = "C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/Models/GradientBoost_model_save.pkl"

adaClf = joblib.load(adaboost)
bnbClf = joblib.load(bnb)
gnbClf = joblib.load(gnb)
extraTreeClf = joblib.load(extraTree)
knnClf = joblib.load(knn)
lrClf = joblib.load(lr)
rfClf = joblib.load(rf)
svmClf = joblib.load(svm)
gbtClf = joblib.load(gbt)

import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
import json

asd=pd.read_csv("C:/Users/Atish Jain/Desktop/WikiVandalism/WikiVandalism/Scripts/testData1.csv")
X=asd.as_matrix(columns= asd.columns[1:13])
y=asd.as_matrix(columns= asd.columns[-1:])

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

adaROC = roc_auc_score(y, adaY)
bnbROC = roc_auc_score(y, bnbY)
gnbROC = roc_auc_score(y, gnbY)
etROC = roc_auc_score(y, etY)
knnROC = roc_auc_score(y, knnY)
lrROC = roc_auc_score(y, lrY)
rfROC = roc_auc_score(y, rfY)
svmROC = roc_auc_score(y, svmY)
gbtROC = roc_auc_score(y, gbtY)

adaROC = adaROC *100
bnbROC = bnbROC *100
gnbROC = gnbROC *100
etROC = etROC *100
knnROC = knnROC *100
lrROC = lrROC *100
rfROC = rfROC *100
svmROC = svmROC *100
gbtROC = gbtROC *100

adaScore = adaScore *100
bnbScore = bnbScore *100
gnbScore = gnbScore *100
etScore = etScore *100
knnScore = knnScore *100
lrScore = lrScore *100
rfScore = rfScore *100
svmScore = svmScore *100
gbtScore = gbtScore *100
''''
adaF1 = roc_auc_score(y, adaY)
bnbF1 = roc_auc_score(y, bnbY)
gnbF1 = roc_auc_score(y, gnbY)
etF1 = roc_auc_score(y, etY)
knnF1 = roc_auc_score(y, knnY)
lrF1 = roc_auc_score(y, lrY)
rfF1 = roc_auc_score(y, rfY)
svmF1 = roc_auc_score(y, svmY)
gbtF1 = roc_auc_score(y, gbtY)

adaRecall = roc_auc_score(y, adaY)
bnbRecall = roc_auc_score(y, bnbY)
gnbRecall = roc_auc_score(y, gnbY)
etRecall = roc_auc_score(y, etY)
knnRecall = roc_auc_score(y, knnY)
lrRecall = roc_auc_score(y, lrY)
rfRecall = roc_auc_score(y, rfY)
svmRecall = roc_auc_score(y, svmY)
gbtRecall = roc_auc_score(y, gbtY)

adaPrecision = roc_auc_score(y, adaY)
bnbPrecision = roc_auc_score(y, bnbY)
gnbPrecision = roc_auc_score(y, gnbY)
etPrecision = roc_auc_score(y, etY)
knnPrecision = roc_auc_score(y, knnY)
lrPrecision = roc_auc_score(y, lrY)
rfPrecision = roc_auc_score(y, rfY)
svmPrecision = roc_auc_score(y, svmY)
gbtPrecision = roc_auc_score(y, gbtY)
'''

result = { "adaboost" : adaScore,
           "bnb" : bnbScore,
           "gnb" : gnbScore,
           "et" : etScore,
           "knn" : knnScore,
           "lr" : lrScore,
           "rf" : rfScore,
           "svm" : svmScore,
           "gbt" : gbtScore,

           "adaboostR" : adaROC,
           "bnbR" : bnbROC,
           "gnbR" : gnbROC,
           "etR" : etROC,
           "knnR" : knnROC,
           "lrR" : lrROC,
           "rfR" : rfROC,
           "svmR" : svmROC,
           "gbtR" : gbtROC,

           }

print(json.dumps(result))