# 参考链接: https://jianghushinian.cn/2021/10/13/Python-%E4%B8%AD%E7%9A%84%E7%B1%BB%E6%96%B9%E6%B3%95%E5%92%8C%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95/
class Student:
    school = "abc"

    # 类方法
    @classmethod
    def hello(cls):
        # cls代表类本身
        print(f"cls:{cls}")
        print(f"hello,{cls.school}")

    # 静态方法,没有隐式参数
    @staticmethod
    def run():
        print(f"run,{Student.school}")

    # 实例方法
    def speak(self):
        self.hello()
        self.run()
        print(f"speak,{self.school}")


def main():
    stu = Student()
    stu.speak()


if __name__ == "__main__":
    main()
