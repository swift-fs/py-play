def add(a, b):
    return a + b


def info():
    print("utils info")


print("utils引入，会执行模块内的代码")

if __name__ == "__main__":
    print("解释器直接执行")
else:
    print("utils 被引入执行:", __name__)
