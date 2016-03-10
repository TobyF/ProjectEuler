import time


def doesChainEnd(start, endcheck):
    while start != 89 and start != 1:
        total = 0
        for digit in str(start):
            total += int(digit) ** 2
        start = total
    if start == endcheck:
        return True
    else:
        return False


count = 0
a = time.time()
for i in range(1, 10000001):
    if doesChainEnd(i, 89): count += 1
    if i % 100000 == 0:
        b = time.time()
        # seconds = int((b-a)*(100-(i//100000)))
        seconds = ((b - a) / (i // 100000)) * (100 - (i // 100000))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print(i // 100000, "percent    %d:%02d:%02d" % (h, m, s), " remaining")
        # a = b

print(count)
