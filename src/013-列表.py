from functools import reduce

# python中，列表也叫list，是一个链表数据结构的实现，可以存储多个任意类型的数据
empty_list = []
name_list = ["小名", "小红"]
age_list = [10, 20]

for name in name_list:
    print(name)


# 增
name_list.append("校长")
name_list.insert(0, "牛")
print(name_list)
# 删除
p1 = name_list.pop()
print(p1)
# 删除指定索引的元素
p2 = name_list.pop(1)
# del name_list[0]
print("p2:", p2)
# 改
name_list[0] = "刘德华"
print(name_list)

# 查
# 取某个元素
print(name_list[0])
# 切片
print(name_list[:1])

# 切片后原始的不变
print(name_list)

# 复制
name_copy_list = name_list.copy()
print(name_copy_list)

# 清空
name_copy_list.clear()
print(name_copy_list)
print(name_list)

# 迭代,对列表里的元素进行遍历
ages = [100, 109, 120, 18]
# enumerate可以获取索引和元素
for index, age in enumerate(ages):
    print(f"index={index},age={age}")

# 迭代器iterator
# 适用于 列表，元组，字符串，集合，字典
# 迭代器是用来遍历目标数据的工具，使用iter()函数可以获取
ages_iter = iter(ages)

# print(next(ages_iter))
# print(next(ages_iter))
# print(next(ages_iter))
# print(next(ages_iter))
# 报错
# print(next(ages_iter))


# for循环也适用于迭代器
for item in ages_iter:
    print(item)

# map函数,可以对列表的每个元素执行一次函数运算,返回一个迭代器

list09 = [19, 10, 11, 22]


def c_s(item):
    return item + 1


iter09 = map(c_s, list09)
# for item in iter09:
#     print(item)

# 迭代器转list
print(list(iter09))


# filter函数
# 过滤列表里的元素，生成一个新的迭代器，不修改原始数据
list09 = [19, 10, 11, 22]


def is_even(num):
    return num % 2 == 0


filtered_list = list(filter(is_even, list09))
print(filtered_list)

# reduce函数
# 对一个列表进行求解，得到一个唯一的结果
list09 = [10, 20, 30, 40]
print(reduce(lambda x, y: x + y, list09))


# 列表解析
# 列表解析是对一个列表进行操作生成新列表的过程
# 语法
# [表达式 for 变量 in 可迭代对象 if 条件]

list10 = [i + 1 for i in list09 if i > 30]
print(list10)
