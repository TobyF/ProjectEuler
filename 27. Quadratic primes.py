def primeCheck(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def quad(a, b, x):
    return x ** 2 + a * x + b


def quadFinder(var_range, BestQuad=[0, 0, 0]):
    for a in range(-var_range, var_range + 1):
        for b in range(-var_range, var_range + 1):
            x = 0
            while primeCheck(quad(a, b, x)):
                x += 1
            if BestQuad[2] < x:
                BestQuad = [a, b, x]
                print("The best polynomial is now: a =", a, " b =", b, " with", x, "primes")


quadFinder(5000)
