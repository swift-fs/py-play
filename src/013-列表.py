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
