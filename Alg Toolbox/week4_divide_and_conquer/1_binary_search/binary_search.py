import math
import sys

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1

def binary_search(keys, low, high, query):
    assert all(keys[i] <= keys[i + 1] for i in range(len(keys)-1))
    assert 0<= len(keys) <= 3 * 10 ** 4
    if low<0 or high>len(keys) or low>high:
        return -1
    elif low<=high:
        mid = low+(high-low)//2
        if keys[mid] == query:
           return mid
        elif query < keys[mid]:
            return binary_search(keys, low, mid-1, query)
        else:
            return binary_search(keys, mid+1, high, query)


    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    search_num = data[n + 2:]
    for x in search_num:
        left, right = 0, n-1
        print(binary_search(a,left, right, x), end = ' ')
       