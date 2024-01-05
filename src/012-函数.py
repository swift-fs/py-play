# 函数作用
# 1. 代码重用
# 2. 函数式编程


# 函数定义
# def 函数名(参数列表):
#     函数体


# 类型不是必须的
def hello(name: str):
    print(f"hello,{name}")


# 没参数
def say():
    print("hello")


# 函数调用
# 函数名(实参)
hello("小红")
say()


# 形参是函数定义中的参数
# 实参是函数调用时传递的参数
# 函数可以定义返回值，返回值是函数调用结束返回的结果
def add(a: int, b: int) -> int:
    return a + b


# 参数和返回值的类型不是必须的
def sub(a, b):
    return a - b


result = add(1, 2)
print(result)

result = sub(10, 8)
print(result)


# 函数的缺省参数(默认参数)
# 具备默认值，在调用的时候可以不用传值
# def 函数名(参数,参数1=默认值1,参数2=默认值2):
#     函数体
def hello(name="小明"):
    print(f"hello,{name}")


hello()
hello("小强")


def say(name, desc="hello"):
    print(f"{desc},{name}")


say("小红")
say("小红", "hi")


# 关键字参数
# 调用的时候不需要按照顺序传递参数
# def 函数名(参数1,参数2):
#     函数体
# 调用 函数名(参数2=值2,参数1=值1)
def say(name, desc="hello"):
    print(f"{desc},{name}")


# 调用时指定参数名
say(desc="hi", name="小红")


# 递归函数
# 函数调用本身
# def recursive_function(parameter):
#     # function body
#     # 递归结束条件，很重要
#     if condition:
#         return base_case_value
#     # 递归调用
#     else:
#         return recursive_function(new_parameter)


def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


print_numbers(10)


def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)


print(sum_numbers(10))


# lambda表达式其实就是定义匿名函数
# lambda 参数列表:表达式
# 不推荐使用lambda，可读性维护性较差


# sum = lambda a, b: a + b
# print(sum(1, 2))


# 等同于
def sum01(a, b):
    return a + b


print(sum01(1, 2))
