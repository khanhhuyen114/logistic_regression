import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(path):
    df = pd.read_csv(path)
    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values    
    return X, y

def standardize(X_tr):
    for i in range(X_tr.shape[0]):
        X_tr[i,:] = (X_tr[i,:] - np.mean(X_tr))/np.std(X_tr)
    return X_tr

def visualize(X,y):
    for i in range(len(X)):
        if y[i] == 1:
            plt.scatter(X[i,0],X[i,1], c = 'r', cmap = 'viridis')
        else:
            plt.scatter(X[i,0],X[i,1], c = 'b')
        plt.xlabel('X 1st dimension')
        plt.ylabel('X 2nd dimension')
        plt.title('Data Visualize')
    plt.show() 