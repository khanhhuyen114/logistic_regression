def score(y,y_hat):
    tp, fn, fp, tn = 0,0,0,0
    for i in range(len(y)):
        if y[i] == 1 and y_hat[i] == 1:
            tp += 1
        elif y[i] == 1 and y_hat[i] == 0:
            fn += 1
        elif y[i] == 0 and y_hat[i] == 1:
            fp += 1
        elif y[i] == 0 and y_hat[i] == 0:
            tn += 1
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2*precision * recall/(recall +  precision)
    accuracy = (tp + tn)/y.shape[0]
    return f1_score , accuracy   

