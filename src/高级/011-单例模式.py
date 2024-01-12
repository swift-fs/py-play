# 单例实现
def singleton_01(cls):
    def inner(*args, **kwargs):
        if getattr(cls, "_instance", None) is None:
            setattr(cls, "_instance", cls(*args, **kwargs))
        return getattr(cls, "_instance")

    return inner


# 单例实现
def singleton_02(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


# @singleton_01
@singleton_02
class Person:
    def __init__(self, name="echp", age=18) -> None:
        print("person init")
        self.name = name
        self.age = age

    def __str__(self):
        return f"person-{self.name}-{self.age}"


def main():
    p1 = Person(name="kiss")
    p2 = Person(name="abc")
    print(p1 is p2)
    print(f"p1:{p1}")
    print(f"p2:{p2}")


if __name__ == "__main__":
    main()
