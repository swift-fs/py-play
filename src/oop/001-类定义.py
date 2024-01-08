class Student:
    # 类变量
    ver = "1.0"

    # 构造函数
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age

    # 实例方法
    def hello(self, msg):
        print(f"hello {msg},my name is {self.name}")


def main():
    print(Student)
    # 类也是对象,Python中,万物皆对象
    print(type(Student))
    print(hex(id(Student)))

    # 实例化
    # 步骤
    # 1. 创建一个物理空对象(初始化内存)
    # 2. 给该物理空对象进行初始化操作，会调用类的构造函数__init__方法
    stu01 = Student(name="xiaomi", age=10)
    stu02 = Student(name="huawei", age=20)
    print(stu01)
    print(stu02)
    print(type(stu01))
    print(isinstance(stu01, Student))

    # 访问类变量
    print(Student.ver)
    print(getattr(Student, "ver"))
    # 类变量被实例对象共享
    print(stu01.ver)
    print(stu02.ver)

    # 修改类变量
    Student.ver = "1.1"
    setattr(Student, "ver", "2.0")
    print(stu02.ver)

    # __dict__存放所有类相关的属性
    print(Student.__dict__)

    # 访问实例变量
    print(getattr(stu01, "name"))
    print(stu01.name)

    # 设置实例变量
    setattr(stu01, "name", "xiaohua")
    print(stu01.name)
    # 调用实例方法
    stu01.hello(msg="一起上学")

    stu01.name = "小米"
    stu01.hello("一起吃饭")


if __name__ == "__main__":
    main()
