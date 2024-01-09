from enum import Enum, unique


# 继承Enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1


# 保证枚举唯一值
@unique
class Status(Enum):
    SUCCESS = 200
    FAIL = 500
    # 会报错，上面200已被使用
    # OK = 200

    # 自定义 == 比较
    def __eq__(self, __value: object) -> bool:
        print("status __eq__ called")
        if isinstance(__value, int):
            return self.value == __value
        if isinstance(__value, str):
            return self.name == str.upper()

        if isinstance(__value, type(self)):
            return self.value == __value.value

    def __lt__(self, __value: object) -> bool:
        print("__lt__ called")

        return False


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

    # 存储所有枚举值
    print(Status.__members__)
    print(Status.FAIL.name)

    for k, v in Status.__members__.items():
        print(f"{k} -> {v.value}")

    print(Status.SUCCESS == 200)
    print(Status.SUCCESS == Status.SUCCESS)
    print(Status.SUCCESS < Status.FAIL)


if __name__ == "__main__":
    main()
