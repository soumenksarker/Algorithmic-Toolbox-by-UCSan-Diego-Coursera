# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    l = sorted(elements)
    #print(l[:4])
    n= len(elements)
    mid = n//2 if n%2==1 else n//2-1
    if elements.count(l[mid])> (mid+1 if n%2==0 else mid):
            return 1
    else:
            return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
