# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    f = [0]*n
    if n<=1:
        return n
    else:
        f[0]=1
        f[1]=1
        for i in range(2,n):
            f[i]=f[i-1]+f[i-2]
    return f[n-1]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
