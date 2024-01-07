# set集合内的元素不能重复
empty_set = set()
set01 = {
    "小红",
    "小名",
}
print(set01)

# 增
set01.add("校长")
set01.add("校长")
print(set01)

print("校长" in set01)

# 删
# 不推荐，不存在报错
set01.remove("小名")
# 推荐，不存在不报错
set01.discard("小名")
print(set01)
# 不推荐，不能指定删除某一个
set01.pop()
print(set01)

# 查
for item in set01:
    print(f"item:{item}")

list01 = [10, 19, 10, 18]
frozenset_set01 = frozenset(list01)
print(frozenset_set01)
print(list(frozenset_set01))

# set并集
set2 = {10, 19}
set3 = {20, 22, 19}
set4 = set2 | set3
set5 = set2.union(set3)
print(set4)
print(set5)

# set交集
set6 = set2 & set3
set7 = set2.intersection(set3)
print(set6)
print(set7)

# set差集
set8 = set2 - set3
set9 = set2.difference(set3)
print(set8)
print(set9)

# set对称差集
set10 = set2 ^ set3
set11 = set2.symmetric_difference(set3)
print(set10)
print(set11)

# set子集
print(set2.issubset(set3))
print({19}.issubset(set3))
