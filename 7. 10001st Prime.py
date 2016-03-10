# What is the 10 001st prime number?
import math


def primeCheck(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def primeGen(x):
    i = 0
    n = 0
    while n < (x - 1):
        i += 1
        if primeCheck(i):
            n += 1
    while True:
        i += 1
        if primeCheck(i):
            return i


print(primeGen(10001))
  
