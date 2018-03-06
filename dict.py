#!/usr/bin/env python

d = {'ff':33,'bob':33,'faa':44}

print(d['ff'])

d['liliangbin'] = 88


print(d)

#  但是假如key不存在就会报错。。。。所以就有了一种判断方法
#  >>> 'key' in d //假如没有就会报错  false  
#  删除还是用的pop方式

d.pop('ff')
print(d)

#  和list来说他的优势在于查询的速度和快，占用的内存更多。  可以说是用内存空间来换取时间的方法


# 不可放入可变的对象


# set该方式和dict很相似，但是他没有对应的value值，但是他可以用来作为交集或是并集计算

# 同时需要传入一个list对象才能创建爱

s = set([1,2,3,4,4,5,6])

print(s)

s.add(9)

s.remove(4)

s1 = set([1,4])

print(s | s1)

print('\n',s&s1)


