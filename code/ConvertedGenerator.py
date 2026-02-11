def squares_gen(n):
    for i in range(n):
        yield i * i

print(list(squares_gen(5)))