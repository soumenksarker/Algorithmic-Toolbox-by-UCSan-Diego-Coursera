# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    w=weights
    value=0
    pwr=[prices[i]/w[i] for i in range(len(prices))]
    if capacity==0 or len(w)==0:
        return 0
    elif len(prices)==1:
        return min(w[0], capacity)*(prices[0]/w[0])
    else:
        while(capacity!=0):
            m = pwr.index(max(pwr))
            amount = min(w[m], capacity)
            capacity-=amount
            value += round(amount*pwr[m], 3)
            pwr.pop(m)
            w.pop(m)
            prices.pop(m)

    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values=[]
    weights=[]
    for i in range (n):
        d0, d1 = map(int, input().split())
        values.append(d0)
        weights.append(d1)
    opt_value = maximum_loot_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

