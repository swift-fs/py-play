from functools import wraps


# 用类定义装饰器
class Decorator(object):
    def __init__(self, func):
        print(f"func:{func}")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        self.func(*args, **kwargs)
        print("after")

    def __repr__(self):
        return self.func.__name__


class DecoratorWithParams(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("before")
            print(f"name:{self.name}")
            func(*args, **kwargs)
            print("after")

        return wrapper


# 函数装饰器
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


# @decorator
# @Decorator
@DecoratorWithParams(name="swift")
def run():
    print(run)


def cls_decorator(cls):
    print("装饰类")
    print(f"cls:{cls}")
    print(f"cls.__dict__:{cls.__dict__}")
    setattr(cls, "ver", "1.0.0")
    return cls


@cls_decorator
class Person:
    def __init__(self) -> None:
        print("person init")


def main():
    # run()
    # print(run)
    person = Person()
    print(person)
    print(person.ver)

    person01 = Person()
    print(person01)
    print(person01.ver)


if __name__ == "__main__":
    main()
