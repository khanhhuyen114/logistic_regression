import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sigmoid import *

class LogisticRegression:
    def __init__(self, X, y):
        self._X = X
        self._y = y.reshape(-1,1)
        self._n = y.shape[0]

    def _initialize(self, X):
        w = np.zeros((X.shape[1]+1, 1))
        n = X.shape[0]
        new_X = np.hstack((np.ones((n,1)), X))
        return w, new_X

    def fit(self, lambda_ = 0.002, iter_ = 100): 
        w, new_X = self._initialize(self._X)

        for i in range(iter_):
            y_hat = sigmoid(new_X @ w)
            dw = new_X.T @ (y_hat - self._y)
            w = w - lambda_ * dw
        return w
    
    def predict(self,X):
        w, new_x = self._initialize(X)
        w = self.fit()
        a = np.dot(new_x, w)
        y_pred = sigmoid(a)
        for i in range(len(y_pred)):
            if y_pred[i] < 0.5 :
                y_pred[i] = 0
            else:
                y_pred[i] = 1
           
        return y_pred