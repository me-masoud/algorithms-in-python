fibs = {0: 0, 1: 1}


def fib(n):
    if n in fibs:
        return fibs[n]

    i = 2
    while i <= n:
        fibs[i] = fibs[i - 2] + fibs[i - 1]
        i += 1

    return fibs[n]


print(fib(200))
