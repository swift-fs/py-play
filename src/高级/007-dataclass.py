import operator
from dataclasses import dataclass, field


class Student(object):
    def __init__(
        self,
        name: str,
        age: int,
        gender: bool,
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender


# 应用场景:暂时只知道用在数据仓库这种场景下
# 其他应用场景有待挖掘，所以不常用
@dataclass(kw_only=True, order=True)
# 初始化后不可修改
# @dataclass(frozen=True)
class Teacher(object):
    # 排序通过第一个字段比较
    sorted_index: int = field(init=False, default=0, repr=False)
    # 可以设置默认值
    name: str = ""
    age: int = 18
    gender: bool = False
    # 不出现在init方法中，可以设置默认值，打印也不出现
    ver: str = field(init=False, default="1.0.0", repr=False)

    # 初始化后调用
    def __post_init__(self):
        self.gender = self.age > 18
        self.sorted_index = self.age


def main():
    teacher = Teacher(name="echo", age=22, gender=True)
    print(teacher)
    teacher02 = Teacher()
    print(teacher == teacher02)
    teachers = [teacher, teacher02]
    # 排序1，使用第一个字段排序(默认)
    print(sorted(teachers))
    print(teachers)
    # 排序2，指定属性排序(最简单)
    print(sorted(teachers, key=operator.attrgetter("age")))
    # 排序3，自定义排序(最通用)
    print(sorted(teachers, key=lambda x: x.age, reverse=True))


if __name__ == "__main__":
    main()
