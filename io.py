# -*- coding: utf-8 -*-


f = open('./high/jjj.md', 'r')
print(f.read())

f.close()

# 如果是因为他的它编码方式的错误我们可以用这种方式来解决
# 如果是图片，或是文件我们可以用'rb'的读取方式来读取
with open('./high/jjj.md', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
with open('./high/liliangbin.md', 'w', encoding='utf-8') as li:
    li.write('hello world')
# 也是和C语言有相同的办法，假设么有这个文件，python自动给你添加进去。

