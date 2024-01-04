# for循环
# for 变量 in 可迭代对象:
#     循环体

# range函数可以生成整数序列
# range(start,stop,step)
# 0-9
r = range(10)
for i in r:
    print(i)
# 15-19
r1 = range(15, 20)
for i in r1:
    print(i)
# 0 2 4
r2 = range(0, 5, 2)
for i in r2:
    print(i)

# while循环
# while 条件:
#     循环体

c = 10
while c < 20:
    print(c)
    c = c + 1

# while True:
#     print("死循环")
