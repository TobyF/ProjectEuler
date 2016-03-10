# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

def fib(n, a=1, b=2):  #n0 = 0 and n1 = 1
    #A function that returns all the fibbonaci numbers to the term that goes over 4,000,000
    yield a
    yield b
    while b < 4000000:
        c = (a + b)
        a = b
        b = c
        yield c


total = 0
for val in fib(1000):
    if val % 2 == 0:
        total += val

print(total)
