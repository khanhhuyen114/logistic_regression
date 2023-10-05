import numpy as np
import pandas as pd
from logistic import *
from handle_data import *
from score import *
from sigmoid import *

X_train, y_train = read_data("./ds1_train.csv")
X_valid, y_valid = read_data("./ds1_valid.csv")


X_train1 = standardize(X_train)
X_valid1 = standardize(X_valid)
logis = LogisticRegression(X_train1, y_train)

y_pred1 = logis.predict(X_train1)
y_pred2 = logis.predict(X_valid1)

tr_f1_score, tr_accuracy = score(y_train, y_pred1)
val_f1_score, val_accuracy = score(y_valid, y_pred2)
print("Training f1 score: \n", tr_f1_score)
print("Training accuracy: \n", tr_accuracy)
print("Validation f1 score: \n", val_f1_score)
print("Validation accuracy: \n", val_accuracy)

visualize(X_train,y_train)