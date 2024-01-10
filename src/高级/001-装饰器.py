from functools import wraps


# 标准写法-不带参数的装饰器
def welcome(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("welcome")
        result = fn(*args, **kwargs)
        return result

    return wrapper


# 标准写法-带参数的装饰器
def welcome01(name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"welcome {name}")
            result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorator


@welcome
@welcome01("kiss")
def my_func(msg: str):
    print(f"hello {msg}")


def main():
    my_func("Swift")
    # f1 = welcome(my_func)
    # f1("Echo")
    print(my_func)


if __name__ == "__main__":
    # 为什么需要装饰器
    # 当很多代码都需要同一种功能时

    # 装饰器的作用
    # 1. 附加功能
    # 2. 修改代码行为
    main()
