#!/usr/bin/env python


print('nihoa')

print("nnn")

name = [x * x for x in range(10)]
#  关于如何快速的生成一个list

print(name)


# 对于在python中有一个函数名同样是一个变量类型的
# 我们可以把它和js对比起来，


def all(x):
    print("niao")
    return x


def f(x, y, z):
    print("开始调用函数")
    return z(x) + z(y)


print(f(22, 44, all))
# 代表他是可以传递函数名的

