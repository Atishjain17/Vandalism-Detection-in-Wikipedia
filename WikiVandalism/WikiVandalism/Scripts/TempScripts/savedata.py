import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
from sklearn.externals import joblib

asd = pd.read_csv("TrainTest.csv")
del asd['totaledit']

#splitting 70 - 30
from sklearn.cross_validation import train_test_split
train, test = train_test_split(asd, test_size=0.3,random_state=3,)

test.to_csv("testData1.csv",index=False, encoding='utf-8')