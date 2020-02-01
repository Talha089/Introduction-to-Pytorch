import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.

def softmax(L):
    expl = np.exp(L)
    sumExpl = np.sum(expl)
    result = []
    for i in expl:
        result.append(i/sumExpl)
    return result
list1 = [5,6,7,8]
ans = softmax(list1)
print(ans)