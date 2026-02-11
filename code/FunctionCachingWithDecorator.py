def memoize(func):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return inner

@memoize
def square(n):
    return n * n

print(square(4))
print(square(4))