class Student:
    def __init__(self, name):
        # 私有实例变量
        self.__name = name

    # 私有实例方法
    def __say_hello(self, msg):
        print(f"hello {msg},my name is {self.__name}")


def main():
    stu = Student("xiaomi")

    # 无法直接访问私有变量和方法
    # 报错
    # print(stu.__name)
    # 报错
    # stu.__say_hello("哈哈")

    # 查看实例对象的__dict__发现有一个_Student__name变量,对应__name变量
    print(stu.__dict__)
    # 可以间接访问私有变量
    print(stu._Student__name)
    # 查看类对象的__dict__发现有一个_Student__say_hello变量,对应__say_hello方法
    print(Student.__dict__)
    # 可以间接访问私有方法
    stu._Student__say_hello("你好")

    # 修改私有变量值
    stu._Student__name = "小红"
    stu._Student__say_hello("你好")

    # 以上例子可以看出,Python中没有绝对的私有限制,可以通过变通的方法设置和访问


if __name__ == "__main__":
    main()
