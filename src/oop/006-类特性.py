# 参考:https://www.liujiangblog.com/course/python/44
class Person:
    def __init__(self, name="echo") -> None:
        print("person __init__ called")
        self.name = name
        self.age = 18

    def say(self) -> None:
        print("hello from person")


# 在子类中如果有与父类同名的成员，那就会覆盖掉父类里的成员。
# 那如果你想强制调用父类的成员呢？使用super()函数！
# 这是一个非常重要的函数，最常见的就是通过super调用父类的实例化方法__init__！


# 语法：super(子类名, self).方法名()
# 需要传入的是子类名和self，调用的是父类里的方法，按父类的方法需要传入参数。
class Student(Person):
    def __init__(self) -> None:
        super(Student, self).__init__(name="swift")
        print("student __init__ called")
        self.school = "Abc"

    # 方法重写
    def say(self) -> None:
        # 可以调用父类方法
        # super(Student, self).say()
        print("hello from student")


class Worker(Person):
    pass


class Stone:
    pass


# 多态:可以使用父类的地方就一定可以使用子类
# 利用这个特性，可以传递父类任意的子类实现
def make_say(person: Person):
    person.say()


def main():
    student = Student()
    print(student.name)
    print(student.school)
    print(isinstance(student, Student))
    print(isinstance(student, Person))

    person = Person()
    print(person.name)
    print(isinstance(person, Student))
    print(isinstance(person, Person))

    print(issubclass(Person, Student))
    print(issubclass(Student, Person))
    print(issubclass(type(student), type(person)))

    stone = Stone()
    print(isinstance(stone, Person))
    print(issubclass(Stone, Person))

    student.say()
    person.say()

    worker = Worker()
    # 没有重写父类方法，自己找不到会向上查找，调用父类方法
    worker.say()

    make_say(student)
    make_say(person)
    make_say(worker)


if __name__ == "__main__":
    main()
