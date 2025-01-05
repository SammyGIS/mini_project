def mygenerator(n):
    for x in range(n):
        yield x**3

value = mygenerator(1000)

print(next(value))
print(next(value))
print(next(value))