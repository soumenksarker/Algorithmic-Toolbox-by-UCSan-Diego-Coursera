import numpy as np
from sys import stdin


def maximum_gold(capacity, weights):
    value = [[0]*(len(weights)+1)]*(capacity+1)
    value=[list(i) for i in zip(*value)]
    #values = [0, 30, 14, 16 , 9]
    #print(value)
    weights=[0]+list(weights)
    #print(weights)
    #v = [1]*(len(weights)+1)
    #weight = weights
    #c = [0]*(len(weights)+1)
    for i in range(len(weights)):
        value[i][0]=0
    for j in range(capacity+1):
        value[0][j]=0

    for i in range(1, len(weights)):
        for w in range(1, capacity+1):
            value[i][w]= value[i-1][w]
            if weights[i]<=w:
                val = value[i-1][w-weights[i]] + weights[i]
                if value[i][w]<val:
                   value[i][w]=val
                else:
                    continue
            else:
                continue



                    #print(value)
    return value[len(weights)-1][capacity]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    print(maximum_gold(input_capacity, input_weights))

