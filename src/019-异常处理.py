# 异常不是语法错误
# 异常是在程序运行中，Python解释器不能处理的问题

# 异常处理语法
# try:
#   code that may raise an exception
# except ExceptionType:
#   # code to handle the exception

try:
    n = 10 / 0
    print("异常产生，此处执行不到")
except Exception as e:
    print(f"异常：{e}")

print("后续代码正常执行")

while True:
    un = input("输入：")
    try:
        un = int(un)
        un = 10 / un
        print("un:", un)
        break
    except ValueError:
        print("请输入整数")
    except ZeroDivisionError:
        print("不能输入0")


try:
    n = 10 / 0
    print("异常产生，此处执行不到")
except (ZeroDivisionError, ValueError):
    print("出错了")
else:
    print("没有产生异常执行")
finally:
    print("有无异常都会执行")
