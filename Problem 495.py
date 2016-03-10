__author__ = 'Toby'
import math
import itertools
# https://projecteuler.net/problem=495
# Let W(n,k) be the number of ways in which n can be written as the product of k distinct positive integers.
#Find W(10000!,30) modulo 1 000 000 007.
n = math.factorial(10000)


def W(n, k):
    pass


def primes(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1

    return factors


def numberSum(count, sum):
    numbers = []
    if count == 0:
        return sum
    else:
        for i in range(sum):
            numbers.append(numberSum(count - 1, sum - i))
    return numbers


for comb in itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3):
    if sum(comb) == 15:
        print(comb)
#print(primes(144))
#print(numberSum(3,20))
print(10**(10**18))