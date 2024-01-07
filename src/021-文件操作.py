# 步骤
# 打开，读写，关闭

from os import path
import os

# 推荐
from pathlib import Path

cwd = Path.cwd()
# 打开
file = open(cwd.joinpath("src", "001-环境.py"), "r")
# 读取
# content = file.read()
# print(content)

for line in file:
    print(line)
# 关闭
file.close()

# 文件不存在会创建
write_file = open(cwd.joinpath("src", "z_content.txt"), "a")
# 写入
write_file.write("第一行")
write_file.close()

# 路径检测
print(path.exists("./001-环境.py"))
print(path.isfile("./001-环境.py"))
print(path.isdir("./001-环境.py"))

p1 = Path("./001-环境.py")
print(str(p1.absolute()))
print(str(p1.resolve()))
print(p1.is_file())
print(p1.is_dir())
print(p1.cwd())

print(Path.cwd())
print(os.getcwd())

# 重命名
# p2 = Path(
#     cwd.joinpath(
#         "src",
#         "z_content.txt",
#     )
# )

# p2.rename("content.txt")

# os.rename()
