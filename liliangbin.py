# filter 函数，用于函数的过滤序列，然后根据返回值来进行取舍。
# 假设为false就会删除。。目的：筛选
def is_odd(n):
    return n % 2 == 1


# 函数对于2取于，，list

r = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))


print(r)