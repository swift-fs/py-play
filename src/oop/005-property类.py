class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    def set_age(self, age: int):
        if age is None or age < 0 or age > 200:
            raise ValueError(f"invalid age {age}")

        self.__age = age

    def get_age(self):
        return self.__age

    def __str__(self) -> str:
        return f"name={self.name}, age={self.__age}"

    age = property(fget=get_age, fset=set_age)


class Teacher:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age is None or age < 0 or age > 200:
            raise ValueError(f"invalid age {age}")

        self.__age = age

    def __str__(self) -> str:
        return f"name={self.name}, age={self.__age}"


class Square:
    def __init__(self, length: int) -> None:
        self.__length = length
        self.__area = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        if length is None or length < 0:
            raise ValueError(f"invalid length {length}")
        self.__area = None
        self.__length = length

    # 只读属性
    @property
    def area(self):
        # 缓存，提高性能
        if self.__area is None:
            self.__area = self.length * self.length
        return self.__area

    # 删除属性,一般不需要
    @area.deleter
    def area(self):
        del self.__area


def main():
    stu = Student(name="小明", age=18)
    stu.age = 10
    stu.set_age(19)
    print(f"stu:{stu}")

    # property装饰器用法，语法糖，等同于上面的代码
    teacher = Teacher(name="老师", age=45)
    print(teacher)
    teacher.age = 18
    print(teacher.age)

    square = Square(length=15)
    print(square.area)
    print(square.area)
    square.length = 18
    print(square.area)
    del square.area
    square.length = 19
    print(square.area)


if __name__ == "__main__":
    main()
