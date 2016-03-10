import math
import itertools


def triangle():
    total = 1
    i = 1
    while True:
        i += 1
        total += i
        yield total


def highestDivisor():
    maxDiv = 0
    for i in triangle():
        x = len(factorCount(i))
        if maxDiv < x:
            maxDiv = x
            print("New max divisors:", maxDiv, "from then  n=", i, "triangle number")
        if x > 499: return i


flatten_iter = itertools.chain.from_iterable


def factorCount(n):
    return set(flatten_iter((i, n // i)
                            for i in range(1, int(n ** 0.5) + 1) if n % i == 0))


print(highestDivisor())


