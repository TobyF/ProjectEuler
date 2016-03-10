def CollatzSequenceLength(n):
    i = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        i += 1
    return i


longest = 0
for i in range(10 ** 6):
    x = CollatzSequenceLength(i)
    if x > longest:
        longest = x
        print("New Top Value Found: ", x, " From Starting Point: ", i)
    
