from math import factorial

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def permGen(digits):
    for a in digits:
        for b in digits:
            if b not in [a]:
                for c in digits:
                    if c not in [a, b]:
                        for d in digits:
                            if d not in [a, b, c]:
                                for e in digits:
                                    if e not in [a, b, c, d]:
                                        for f in digits:
                                            if f not in [a, b, c, d, e]:
                                                for g in digits:
                                                    if g not in [a, b, c, d, e, f]:
                                                        for h in digits:
                                                            if h not in [a, b, c, d, e, f, g]:
                                                                for i in digits:
                                                                    if i not in [a, b, c, d, e, f, g, h]:
                                                                        for j in digits:
                                                                            if j not in [a, b, c, d, e, f, g, h, i]:
                                                                                yield a, b, c, d, e, f, g, h, i, j


i = 0
for x in permGen(digits):
    i += 1
    if i % 10000 == 0:
        print("You are ", i // 10000, "% through")
    if i == 1000000:
        print(x)
    
                                                                                    
