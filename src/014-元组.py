# tuple也是一个list，但是内容不能改变，类似其他语言的数组
# 定义tuple，使用()
t = (1, 2, 5, 9, 0)
print(t)
print(len(t))

empty_t = ()
one_t = (2,)
default_t = 1, 2, 5
print(default_t)

for item in default_t:
    print("item:", item)

print("type:", type(default_t))


def t_func():
    return 404, "not found"


r_t = t_func()
print(r_t)
# 解包，适合序列解包
a, b = t_func()
print("a:", a)
print("b:", b)

print("r_t 0:", r_t[0])

# 类型转换
# list转tuple
list01 = [1, 2, "哈"]
tuple01 = tuple(list01)
print(tuple01)
# tuple转list
list02 = list(tuple01)
print(list02)

# tuple连接
tuple03 = tuple01 + tuple01
print(tuple03)

# 元组是否包含指定值
print(1 in tuple03)
