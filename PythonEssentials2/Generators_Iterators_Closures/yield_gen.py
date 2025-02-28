def fun(n):
    for i in range(n):
        yield i
 
 
for v in fun(5):
    print(v)

print()
print()

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for v in powers_of_2(8):
    print(v)

print()
print()

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

