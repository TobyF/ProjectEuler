def fib(n, a=0, b=1, count=1):  # n0 = 0 and n1 = 1
    #A function that returns all the fibbonaci numbers to the nth term sequentially 
    #print(a)
    #print(b)
    while True:
        count += 1
        c = (a + b)
        a = b
        b = c
        if len(str(c)) == n: return count, c


print(fib(1000))
