class MyDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    # __str__() 方法返回对象字符串表示形式。此方法由内置的 print() 、 str() 和 format() 函数调用。
    # 如果您没有为类定义 __str__() 方法，则内置对象实现将调用 __repr__() 方法。
    # 主要提供给用户
    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}"

    # __repr__() 方法返回对象的信息更丰富的或官方的字符串表示形式。
    # 该方法由内置的 repr() 函数调用。
    # 如果可能，返回的字符串应该是可用于重新创建对象的有效 Python 表达式。在所有情况下，该字符串都应该提供信息且明确。
    # 主要提供给开发者
    def __repr__(self) -> str:
        return f"MyDate:{self.year}-{self.month}-{self.day}"

    # __eq__() 方法用于比较两个对象是否相等。（实现对象的 == 比较）
    def __eq__(self, __value: object) -> bool:
        print("eq is called")
        if not isinstance(__value, MyDate):
            return False
        return hash(self) == hash(__value)

    # __hash__和__eq__方法是共存的
    # __eq__相等的两个对象必须具有相同的__hash__
    def __hash__(self) -> int:
        print(f"{self} -> hash called")
        return hash((self.year, self.month, self.day))

    def __bool__(self):
        print("bool is called")
        return self.year > 2021

    # 对象被垃圾回收之前调用
    def __del__(self):
        print("del is called")


def main():
    my_date01 = MyDate(2023, 10, 20)
    # 调用对象的__str__方法
    print(my_date01)
    # 调用对象的__repr__方法
    print(repr(my_date01))
    # 调用对象的__del__方法
    del my_date01

    my_date02 = MyDate(2023, 1, 1)

    print(my_date02)
    my_date03 = MyDate(2023, 1, 1)
    print(my_date03)
    # is 比较两个对象是否为同一个
    print(my_date02 is my_date03)
    # == 调用对象的__eq__方法
    print(my_date02 == my_date03)
    # 调用对象的__hash__方法
    print(hash(my_date02))
    print(hash(my_date03))
    # 调用对象的__bool__方法
    print(bool(my_date03))


if __name__ == "__main__":
    main()
