def busStop(deno, nume=10, values=[]):
    mod = None
    while mod not in values:
        values.append(mod)
        mod = nume // deno
        print(mod, deno, nume)
        deno = mod * 10
    return values


print(busStop(5))
