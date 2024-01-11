# 使用元类就可以多看看该例子
class Prop:
    def __init__(self, prop_name: str) -> None:
        # 注意要f"_{prop_name}"，否则循环引用死循环异常
        self._prop_name = f"_{prop_name}"

    def get(self, obj):
        if not hasattr(obj, self._prop_name):
            return hex(id(obj))
        return getattr(obj, self._prop_name)

    def set(self, obj, val):
        setattr(obj, self._prop_name, val)


class Human(type):
    def __new__(cls, base, name, attrs, **kwargs):
        cls_ = super().__new__(cls, base, name, attrs)
        for key, val in attrs.items():
            if key == "props":
                for prop_name in val:
                    p = Prop(prop_name)
                    # 定义实例属性
                    p_obj = property(fget=p.get, fset=p.set)
                    setattr(cls_, prop_name, p_obj)

        return cls_


class Student(object, metaclass=Human):
    props = ["name", "age"]

    def __str__(self):
        return f"stu-{self.name}-{self.age}"


def human_decorator(cls):
    print(cls.__dict__)
    return Human(cls.__name__, cls.__bases__, dict(cls.__dict__))


# 装饰器使用元类,尽量不使用,不利于调试
@human_decorator
class Teacher(object):
    props = ["name", "age"]

    def __str__(self) -> str:
        return f"teacher-{self.name}-{self.age}"


def main():
    stu = Student()
    # stu.name = "swift"
    # stu.age = 10

    stu1 = Student()
    # stu1.name = "swift001"
    # stu1.age = 100
    print(f"stu:{stu}")
    print(f"stu1:{stu1}")
    # print(f"stu name:{stu.name}")

    teacher = Teacher()
    teacher.name = "swift"
    print(f"teacher:{teacher}")
    teacher01 = Teacher()
    print(f"teacher01:{teacher01}")
    print("end")


if __name__ == "__main__":
    main()
