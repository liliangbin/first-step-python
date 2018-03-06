#!/usr/bin/env python

classmates = ['lili','nn','ff']

print(len(classmates))

classmates.append('adam')


print(classmates[3])

classmates.pop()

print(classmates)

classmates.insert(2,'ff')
print(classmates)


# classmates.insert(1,'nn')   //表示插入某个位置一个值

# 同样有着删除的方法  pop 删除末尾 删除指定位置  pop（i）。i就是需要删除的位置

# list里面的元素可以是不同类型的



