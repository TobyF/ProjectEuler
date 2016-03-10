# 0,   2,4,6,8,  12,16,20,24


def locFinder(spiralHeight):
    spiralLength = spiralHeight ** 2
    loc = 0
    total = 0
    total += loc + 1
    for i in range((spiralHeight + 1) // 2):
        for x in range(4):
            if loc != loc + (2 * i):
                loc = loc + (2 * i)
                total += loc + 1
    return total


print(locFinder(1001))

