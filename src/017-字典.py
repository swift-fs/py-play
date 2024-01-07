# 字典dict用来存放键值对
empty_dict = {}

person_dict = {
    "name": "swift",
    "age": 10,
    "gender": "male",
}

print(person_dict)
print(type(person_dict))
# 增
person_dict["height"] = 180
person_dict["weight"] = 120
print(person_dict)
# 删
del person_dict["weight"]
print(person_dict)
# 改
person_dict["age"] = 20
print(person_dict)
# 查
# 不推荐,获取不存在的key会报错
print(person_dict["name"])
# 推荐，获取不存在的key不报错，也可以设置默认值
print(person_dict.get("name"))
print(person_dict.get("weight", "默认值"))

# 遍历
for key in person_dict:
    print(key, person_dict[key])

for key in person_dict.keys():
    print(key, person_dict[key])

for val in person_dict.values():
    print(val)

for key, val in person_dict.items():
    print(key, val)


person = list(person_dict.items())
print(person)
person_dict01 = dict(person)
print(person_dict01)

# 字典解析
new_dict = {f"{key}-01": val for key, val in person_dict.items() if key == "name"}
print(new_dict)

# 字典合并

dict01 = {
    "name": "echo",
    "age": 19,
}

dict02 = {
    "age": 18,
}

dict03 = {**dict01, **dict02}
print(dict03)
