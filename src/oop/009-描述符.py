# 参考:https://docs.python.org/zh-cn/3/howto/descriptor.html
# descriptor
# 挺重要的概念,很多开源库都会使用到
# 描述符的定义很简单，实现了下列任意一个方法的 Python 对象就是一个描述符（descriptor）：
# __get__(self, obj, type=None)
# __set__(self, obj, value)
# __delete__(self, obj)

# self 是当前定义的描述符对象实例。
# obj 是该描述符将作用的对象实例。
# type 是该描述符作用的对象的类型（即所属的类）。

# 描述器让对象能够自定义属性查找、存储和删除的操作。

from pathlib import Path


# 返回常量的描述器
class Ten:
    def __get__(self, obj, objtype=None):
        print("get called")
        print(obj)
        print(objtype)
        return 10


# 动态查找
class DirectorySize:
    def __get__(self, obj, objtype=None):
        p = Path(__file__).parent.parent.parent
        p: Path = p / obj.dirname
        return len(list(p.glob("*")))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname: str) -> None:
        self.dirname = dirname


class RequireAge:
    def __get__(self, obj, objtype=None):
        if obj is None:
            raise AttributeError("can't get age from class")
        value = obj._age
        return value

    def __set__(self, obj, value):
        print("设置年龄:", value)
        if value < 0:
            raise ValueError(f"invalid age {value}")
        obj._age = value

    # 当一个类使用描述器时，它可以告知每个描述器使用了什么变量名。
    def __set_name__(self, owner, name):
        print("属性名字:", name)
        self.name = name


class Person:
    age = RequireAge()

    def __init__(self, name, age=1):
        self.name = name
        self.age = age  # Calls __set__()

    def increase(self):
        self.age += 1


# 要使用描述器，它必须作为一个类变量存储在另一个类中
class Square:
    x = Ten()
    y = Ten()
    z = 5


# 完整例子,完全动态托管属性


class RequireStr:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        setattr(obj, self.name, value)


class Student:
    name = RequireStr()
    gender = RequireStr()

    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender


def main():
    # 入门
    square = Square()
    print(square.x)
    print(square.y)
    print(square.z)
    print(Square.__dict__)

    # 动态获取指定文件夹下的子文件数量
    print(Directory("src/oop").size)
    print(Directory("src").size)

    # 托管属性 -> 托管对实例数据的访问
    # 描述器被分配给类字典中的公开属性，而实际数据作为私有属性存储在实例字典中。
    # 当访问公开属性时，会触发描述器的 __get__() 和 __set__() 方法。
    p = Person("swift")
    p.age = 10
    p.increase()
    print(p.age)

    p1 = Person("echo")
    p1.age = 19
    p1.increase()
    print(p1.age)

    # 互不影响，都存在自己的实例字典中
    print(f"p age: {p.age}")
    print(f"p1 age: {p1.age}")
    print(p.__dict__)
    print(p1.__dict__)

    # 报错
    # print(Person.age)

    # 完整的例子
    student = Student(name="swift", gender="male")
    student01 = Student(name="echo", gender="female")
    print(f"student: {student.name}, {student.gender}")
    print(f"student01: {student01.name}, {student01.gender}")


if __name__ == "__main__":
    main()
