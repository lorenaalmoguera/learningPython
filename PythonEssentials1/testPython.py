my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)


nums = [1, 2, 3]
vals = nums


a = 1 // 2

print(a)

my_list = [x * x for x in range(5)]
 
 
def fun(lst):
    del lst[lst[2]]
    return lst
 
 
print(fun(my_list))

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

nums = [1, 2, 3]
vals = nums
del vals[:]

print(vals)
print(nums)




dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

lst = [i for i in range(-1, -2)]

print(lst)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)



print(fun(0, 3))


dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

foo = (1, 2, 3)
foo.index(0)


