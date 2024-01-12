# 参考:https://www.geeksforgeeks.org/python-scope-of-variables/
# 全局变量
msg = "global msg"


def local_func():
    # 局部变量
    msg = "local msg"
    print(msg)

    def inner_func():
        # 函数嵌套函数
        # 该关键字声明一个变量以指向外部封闭函数的变量（在嵌套函数的情况下）
        nonlocal msg
        msg = "inner msg"
        print(msg)

    inner_func()
    print(msg)


def global_func():
    # 局部作用域定义/修改全局变量
    global msg
    msg = "abc"
    print(msg)


# 无关键字修饰时，默认情况下
# 嵌套函数 -> 函数内 -> 全局以此查找
local_func()
print(msg)
global_func()
print(msg)
