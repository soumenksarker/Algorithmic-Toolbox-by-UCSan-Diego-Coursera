# python3
"""fibonacci number, golden ratio(1.618) is the ratio between two
consecutive fibonacci number, last digit cyles is 60
(modular arithmatic, euler_toteint function, Fermat's
little theorem. if gcd(a,n) = 1, then aφ(n) ≡ 1 (mod n). For example,
φ(10)=4, so if gcd(7,10) = 1, then 7^4 ≡ 1 (mod 10) thus it's true for Fn+15=7Fn(mod 10) base on
chiness remainder theorem after computing (mode 2, mod 3, mode 5) and finally x=10+ 7*4(where 4 is the k value)
where 7 and 10 are co-prime for the sequence x)"""
# python3
import math


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10
#efficient implementation
f=[0]*61
def fibonacci_number(n):
    f[0]=0
    f[1]=1
    for i in range(2,60):
        f[i]=(f[i-1]+f[i-2])%10
    return f[n%60]
def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    return fibonacci_number(n)



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

