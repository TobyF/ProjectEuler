import math


def primeCheck(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primeGen(x):
    for i in range(x):
        if primeCheck(i):
            yield i


total = 0
for prime in primeGen(2000000): total += prime
print(total)
