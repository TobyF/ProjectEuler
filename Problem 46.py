__author__ = 'Toby'
def goldbachContra():
    i = 4
    while True:
        current = False
        if i%2 == 1:
            if not isPrime(i):
                for possiblePrime in range(2,i):
                    if isPrime(possiblePrime):
                        if (((i-possiblePrime)/2)**0.5)%1 != 0:
                            #print(str(i)+"="+str(possiblePrime)+"+ 2x"+str(((i-possiblePrime)/2)**0.5))
                            current = True
                if not current: print(str(i)+"="+str(possiblePrime)+"+ 2x"+str(((i-possiblePrime)/2)**0.5))
        i+=1
        if i%100 == 0:
            print(i)
def isPrime(Number):
    return 2 in [Number,2**Number%Number]

print(goldbachContra())