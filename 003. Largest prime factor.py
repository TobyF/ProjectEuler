# What is the largest prime factor of the number 600851475143 ?

import math

# #def largestPrimeFactor(x):
##    primeFactors = []
##    progress = 0
##    for i in range(1,x+1):
##        if x%i == 0 and primeChecker(i):
##            primeFactors.append(i)
##        Check = round(i/x,5)
##        if Check > progress:
##            print(progress,"%")
##            progress = Check
##    if len(primeFactors) == 0:
##        return "There ae no Prime Factors"
##
##    return max(primeFactors)
##
##print(largestPrimeFactor(600851475143))

def primeCheck(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def primeGen(n):
    for i in range(n // 2):
        if primeCheck(i):
            yield i


def largestPrimeFactor(x):
    if primeCheck(x):
        return x, " is already prime!"
    for val in primeGen(x):
        while x % val == 0:
            x = x / val
            print(val, "is a prime Factor, dividing to now check ", x)
            if primeCheck(x):
                print("Largest Prime Found To Be: ", x)
                return x


largestPrimeFactor(62129)

