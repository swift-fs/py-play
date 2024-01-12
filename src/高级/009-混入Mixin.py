# 混入
# 一般把通用功能抽离到Mixin类中
# 因为python支持多继承，所以可以把通用功能抽离到Mixin类中


class RunMixin(object):
    def run(self):
        print("run")


class SleepMixin(object):
    def sleep(self):
        print("sleep")


# 多继承
class Person(RunMixin, SleepMixin, object):
    def __init__(self, name="un", age=18) -> None:
        self.name = name
        self.age = age


def main():
    person = Person()
    person.sleep()
    person.run()


if __name__ == "__main__":
    main()
