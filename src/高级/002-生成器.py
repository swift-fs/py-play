# 生成器也是一个可迭代的对象
# 动态生成数据，节省内存
# 在python中，能用迭代器或者生成器处理的数据，尽量用
def hello():
    print("hello")
    yield 1
    print("world")
    yield 2
    print("kiss")
    yield 3
    print("bye")


def main():
    gen = hello()
    print(gen)
    # i = next(gen)
    # print(i)
    # i = next(gen)
    # print(i)
    # i = next(gen)
    # print(i)

    # print(list(gen))

    # for i in gen:
    #     print(i)
    # print(type(gen))

    # square = Square(20)
    # r = next(square)
    # print(r)
    # r = next(square)
    # print(r)


# 迭代器实现
class Square:
    def __init__(self, count):
        self.count = count
        self.current = 0

    def __iter__(self):
        print("迭代器执行了")
        return self

    def __next__(self):
        if self.current < self.count:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    main()
