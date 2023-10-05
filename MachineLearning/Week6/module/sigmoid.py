import numpy as np
def sigmoid(x):
    z = 1/(1 + np.exp(-x))
    return z