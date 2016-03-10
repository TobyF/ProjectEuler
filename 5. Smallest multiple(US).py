# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

n = 20


def LCM(n):
    for i in range(2, math.factorial(n)):
        LCM = True
        x = 1
        while x <= n and LCM == True:
            x += 1
            if i % x != 0:
                LCM = False
        if LCM == True:
            print("LCM: ", i)
            return i


LCM(n)
