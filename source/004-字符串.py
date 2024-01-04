# 字符串就是用单引号或者双引号引用的一串字符序列
# 一般情况下推荐使用双引号
msg = "12589"
msg = "12589"
msg = """125678"""
print(msg)

# 转义字符:反斜杠\用来在字符串中进行转义,表达为其他的含义
# 常用的转义字符:\n换行 \r回车 \\反斜杠 \'单引号 \"双引号
msg = "你好呀!\n中国!\n'天才少年' \\n \\r \\t \\\" \\' "
print(msg)

# 原生字符串:r字符串,内容保留原样
msg = r'你是谁:"韩梅梅"'
print(msg)

# 字符串连接
# 使用+号
# 字符串 空格 字符串
greeting = "hello"
name = " world"
msg = greeting + name
print(msg)
msg = "hello" " world!"
print(msg)

# 功能字符串
# 字符串 * 整数
msg = "hello" * 3
print(msg)
# f字符串,格式化字符串,可以在字符串中使用{变量}插入其他值
msg = f"hello {name}"
print(msg)

# 获取字符串长度
print(len(msg))
# 获取字符串中的单个字符
print(msg[0])
# 字符串切片,获取字符串的子串,左闭右开区间
print(msg[0:3])
