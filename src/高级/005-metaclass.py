# 元类
# type类就是一个元类
# 元类是用来创建类的
# type就是所有类默认的metaclass
# 可以在定义类的时候指定metaclass
# 当希望创建一个类就自带了很多方法或属性，不仅仅局限静态方法时，就可以优先考虑元类

# 平时用的也不多，除非写的代码对动态性要求极高，适合各个业务场景


def hello(self):
    print("hello")
    print(type(self))


# 定义一个元类
# 必须继承type
class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        # 在创建类之前可以做一些额外的操作
        print("Creating class:", args)
        cls_ = super().__new__(cls, *args)
        print(type(cls_))
        print(f"kwargs:{kwargs}")
        # 动态定义类方法/对象属性
        if kwargs:
            for key, val in kwargs.items():
                setattr(cls_, key, val)
        # 定义一个对象方法
        setattr(cls_, "hello", hello)
        # 定义了一个类属性
        setattr(cls_, "static_age", 10)
        # 创建类
        return cls_


# 使用元类创建类
class MyClass(object, metaclass=MyMeta, country="china"):
    pass


def main():
    mc = MyClass()
    mc.hello()
    print(mc)
    print(MyClass.static_age)
    print(MyClass.country)


if __name__ == "__main__":
    main()
