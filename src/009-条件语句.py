# if语句,条件为真,执行下面的语句块
# 条件为假,继续往下判断elif
# 都为假执行else
if 10 < 20:
    print("执行了")
elif 10 > 20:
    print("没有执行")
else:
    print("没有执行")

# 三元运算符 值1 if bool else 值2
# 等同于其他语言中的 bool ? 值1:值2
name = "hello" if 10 > 20 else "world"
print(name)
