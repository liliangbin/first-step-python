from functools import reduce


def fx(x):
    return x * x


r = map(fx, [1, 2, 3, 4, 5])
print(list(r))

L1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return name[0].upper() + name[1:].lower()


L2 = list(map(normalize, L1))

print(L2)

L3 = [1, 2, 3, 4, 5, 6]


def s(x, y):
    return x * y


def prod(L):
    return reduce(s, [1, 2, 3, 4])


# L4 = reduce(s, L3)
# print(list(L4))
# map()函数返回的是一个迭代器，数据是不会迭代的，，接受的是一个迭代类型
def add(x, y):
    return x + y


r = reduce(add, L3)
# 最后的时候返回的时候就是一个迭代器类型的
# reduce只要是个叠加运算，，
print(r)


def normai(x):
    return x[0].upper() + x[1:].lower()
