# break 中断当前循环
# while True:
#     if condition:
#         break
num = 0
while True:
    num = num + 1
    if num > 10:
        break

# continue 循环跳到下一次
# while True:
#     if condition:
#         continue
num01 = 1
while True:
    num01 = num01 + 1
    if num01 < 10 and num01 % 2 == 1:
        continue
    elif num01 > 10:
        break
    print(num01)

# pass 什么都不干，占位语句，待实现的代码
while num01 < 20:
    num01 = num01 + 1
    # 待实现
    pass
