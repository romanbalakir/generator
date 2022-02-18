def generate(max):
    a, b = 0, 2
    while a < max:
        yield a
        a, b = b, a + b


for x in generate(999):
    print(x)