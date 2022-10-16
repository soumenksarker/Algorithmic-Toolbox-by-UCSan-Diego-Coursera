# python3
import random
import sys
from random import randint

def partition3(a, l, r):
    #Divide and conquer
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i],a[m1] = a[m1],a[i]
            m1+=1
            m2+=1
            a[i],a[m2] = a[m2],a[i]
        elif a[i] == x:
            m2+=1
            a[i],a[m2] = a[m2],a[i]
   # a[l],a[m1] = a[m1],a[l]
    return m1,m2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    j,k = partition3(a, l, r)
    randomized_quick_sort(a, l, j-1)
    randomized_quick_sort(a, k+1, r)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements)-1)
    print(*elements)
