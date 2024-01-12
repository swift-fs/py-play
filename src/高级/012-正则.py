# Python中使用正则
# 正则可以用来
# 1.匹配验证
# 2.搜索指定文本

# python内置提供了正则表达式的支持模块re
import re


# 搜索第一个满足需求的文本
def test_search():
    result = re.search(r"\d+", "我今年15岁了，身高180")
    print(result)


# 匹配验证
def test_match():
    # 开头匹配
    result_01 = re.match(r"\d+", "1500")
    # 完全匹配
    result_02 = re.fullmatch(r"\d+", "1500abc")
    print(result_01)
    print(result_02)


# 查找所有匹配文本
def test_find():
    result = re.findall(r"\d+", "我今年15岁了,身高180，电话110")
    print(result)


# 查找所有匹配文本，返回的是迭代器，一般用findall即可
def test_finditer():
    result = re.finditer(r"\d+", "我今年15岁了,身高180，电话110")
    for i in result:
        print(f"i:{i}")


# 编译 -> 使用
def test_compiler():
    # 编译正则表达式
    pattern = re.compile(r"\d+")
    # 使用正则表达式
    result = pattern.findall("我今年15岁了，身高180")
    print(result)


def main():
    test_search()
    test_match()
    test_find()
    test_finditer()
    test_compiler()


if __name__ == "__main__":
    main()
