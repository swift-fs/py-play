# 上下文管理器，英文名称为 context manager
# 上下文管理器是一个对象
# 定义了运行时的上下文
# 使用with语句来执行
from pathlib import Path


class CtxTest:
    def __init__(self, count):
        self.count = count

    def __enter__(self):
        print("enter")
        return self.count

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        print(f"exc_type:{exc_type}")
        print(f"exc_val:{exc_val}")
        print(f"exc_tb:{exc_tb}")
        return True


def main():
    # 语法
    # with context as ctx:
    #     pass
    # 上下文对象已被清除

    # 例子一
    with open("test.txt", "w") as f:
        f.write("hello")
    # 例子二
    with Path("test.txt").open(encoding="utf-8") as f:
        print(f.read())

    # 自定义上下文管理器，必须实现__enter__和__exit__
    # __enter__安装上下文，可以返回对象
    # __exit__上下文执行完毕会调用，可以做一些释放资源的工作等
    with CtxTest(12) as c:
        print(c)
    print("程序执行结束")
    # 应用场景
    # 开-关
    # 加锁-解锁
    # 启动-停止
    # 改变-重置
    # 只要是两个状态，就可以使用上下文管理器


if __name__ == "__main__":
    main()
