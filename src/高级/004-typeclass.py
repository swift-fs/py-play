class Student:
    def greeting(self):
        print("Hello student")


print(Student)
print(type(Student))

print(isinstance(Student, type))


class_body = """
def greeting(self):
    print("Hello customer")
def jump(self):
    print("jump")
"""
class_dict = {}


exec(class_body, globals(), class_dict)
print(class_dict)
# 动态定义类
Customer = type("Customer", (object,), class_dict)
print(Customer)
c = Customer()
c.greeting()
c.jump()


def hi():
    a = 10
    b = 20
    print(locals())


hi()
