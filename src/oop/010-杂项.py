# 函数可以接受任意参数
# args 位置参数
# kwargs 关键字参数
from typing import Self


def excute(*args, **kwargs):
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")
    ext_kwargs = {**kwargs, "ver": 1.0}
    print(f"ext_kwargs:{ext_kwargs}")


# 参考:https://www.cnblogs.com/lincappu/p/13520212.html
class MyInt(int):
    def __init__(self, val: int):
        print("init called")
        print(self)
        print(val)

    def __new__(cls, val: int) -> Self:
        print("new called")
        obj = super().__new__(cls, val * 2)
        return obj


class Student:
    def __new__(cls, name, age) -> Self:
        print(f"new:{name},{age}")
        obj = super().__new__(cls)
        obj.name = name
        obj.age = age
        return obj


# 自定义异常
class InvalidAge(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def main():
    excute("10")
    excute("swift", True)
    excute("Abc", True, age=10, name="swift")

    stu = Student(name="jack", age=19)
    print(f"stu:{stu}")

    i = MyInt(10)
    print(f"i:{i}")
    print(isinstance(i, int))
    print(type(i))

    age = -2
    try:
        if age < 0:
            raise InvalidAge("age must > 0")
    except InvalidAge as e:
        print(e)


if __name__ == "__main__":
    main()
