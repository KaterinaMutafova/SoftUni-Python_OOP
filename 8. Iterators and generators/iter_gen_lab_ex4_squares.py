# squares = lambda n: (i ** 2 for i in range(1, n + 1))

def squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


print(list(squares(5)))