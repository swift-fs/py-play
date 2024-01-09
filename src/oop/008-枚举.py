from enum import Enum


# 继承Enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Student:
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender


def main():
    print(type(Gender))
    print(Gender.MALE)
    # 枚举名
    print(Gender.MALE.name)
    # 枚举值
    print(Gender.MALE.value)
    stu = Student("swift", Gender.MALE)
    print(stu)

    # 通过枚举名生成枚举
    stu.gender = Gender["FEMALE"]
    print(stu.gender)
    # 通过枚举值生成枚举
    stu.gender = Gender(0)
    print(stu.gender)
    print(Gender["MALE"] == Gender.MALE)


if __name__ == "__main__":
    main()
