def twentycheck(x):
    for i in range(1, 22):
        if int(x) % i != 0:
            return False
    return True


def smallest():
    x = 1
    while twentycheck(x * 2520) != True: x += 1
    return x * 2520


print(smallest())
