# 什么是模块
# 可以认为每一个py文件都是一个模块
# 一个模块可以包含函数，类，变量等多种信息

# 引用其他模块
# import 模块名
# from 模块名 import 函数，类，变量
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 函数 as 别名

# 不推荐，代码可读性低
# from z_utils import *
import z_utils
import z_utils as utils
from z_utils import add, info
from z_utils import add as utils_add
import sys
from z_childs import child as z_child
from z_childs.sub_childs import schild

print(z_utils.add(10, 20))
print(utils.add(10, 20))
print(add(10, 20))
print(utils_add(10, 20))
info()

# 模块的搜索路径
# 1. 搜索当前路径
# 2. 搜索环境变量PYTHONPATH中定义的路径
# 3. 搜索安装Python时配置的依赖安装路径(默认为为site-packages)
# 搜索路径被保存在sys.path变量中
for path in sys.path:
    print(path)

# 当执行一个程序文件时，__name__变量就是__main__
# 当一个模块文件被其他文件引入使用时，__name__变量就是该模块的名字

# 什么是包
# 包对应文件夹
# 每一个包文件夹下需要一个__init__.py文件
# 可以使用 from ... import ...来引入不同包中的模块
print(z_child.color())

print(schild.green())

# 获取命令行参数
print(sys.argv)
