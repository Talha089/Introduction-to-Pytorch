import numpy as np

def cross_entropy(Y,P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


listy = [1,0,1,1]
listp = [0.4,0.6,0.1,0.5]

cross_entropy_answer = cross_entropy(listy,listp)
print(cross_entropy_answer)