# fib [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fib(n):
    if n < 2:
        return n
    
    return fib(n - 2) + fib(n - 1)


# CACHE THAT BAD BOY
cache = {}
def fib_cache(n):
    if n < 2:
        return n
    elif n in cache:
        return cache[n]

    value = fib_cache(n - 1) + fib_cache(n - 2)
    cache[n] = value
    return value

print(fib_cache(int(input())))
print(cache)