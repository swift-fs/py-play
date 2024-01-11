# 任何class在内存里就是一个type类的对象
# python使用type类来创建其他的class
# 语法: type(class_name,parents,class_dict)
# 理论上来讲，可以使用type来动态创建class

from pathlib import Path


class Student:
    def greeting(self):
        print("hello student")


def main():
    print(type(Student))
    print(isinstance(Student, type))
    # 动态内容，可以通过其他加载过来，比如用户上传的文本文件
    dynamic_content = Path(__file__).parent / "dynamic_content.txt"
    class_body = dynamic_content.read_text(encoding="utf-8")
    class_dict = {}
    # 可以把一个python语法的字符串内容转换为一个字典
    exec(class_body, globals(), class_dict)
    Customer = type("Customer", (object,), class_dict)
    customer = Customer()
    customer.greeting()


if __name__ == "__main__":
    main()
