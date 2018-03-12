# 函数主要的目的是对于i数据的排序
# 函数直接经行的是从小到大的排序。
# 同时不会对于数据的删除
rr = sorted([1, 2, 3, 4, 4, 6, 6])
print(rr)

#  同样可以通过某个参数排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[0].lower()
