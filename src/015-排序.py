# sort函数,会改变原列表
l1 = [10, 2, 19]
l1.sort()
print(l1)

l2 = [11, 19, 3]
l2.sort(reverse=True)
print(l2)

# 定制排序,使用key指定排序函数
l3 = [("小红", 19), ("小强", 8), ("小明", 10)]


def c_s(item):
    return item[1]


l3.sort(key=c_s, reverse=True)
print(l3)


# sorted函数,不会改变原始列表,用法和sort保持一致
l4 = [11, 19, 3]
l5 = sorted(l4)
print(l5)
print(l4)
