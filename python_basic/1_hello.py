# 计算结果
import math


# 第一课
print("hello world")


# 字符串拼接
print("hello" + " world")
# 单引号
print('hello world')
# 反斜杠表示特殊字符，\表示转义符
print("hello\"world")
# 换行
print("hello\nworld")
# 三引号跨行字符串,单引号、双引号都可以
print("""人生的乐趣便是无尽的探索，
并感知其中的意味，
爱便在其中""")


# 变量赋值
my_love = "123888574"
print("拨打：" + my_love)
# 变量覆盖
my_love = "354567766"
print("拨打：" + my_love)
# 变量定义【见名知义、英文命名：下划线命名、驼峰命名】
# 计算结果【整数、浮点数、字符串】【次方运算】
print(math.sin(1))
a = -1
b = -2
c = 3
x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
print("The result is ", x1, " ", x2)


# 注释【做解释：#、三引号】
"""
这是注释
"""


# 数据类型【字符串、整数、浮点数、布尔类型、空值、列表、字典】
"""
字符串【单引号、双引号、len()、转义字符、字符索引("sad"[2] => d)、】
整数、浮点数
布尔类型【真(True)、假(False)】
空值类型【None(不是0、""、False)、type()[判断数据的类型]】
"""
s = "Great American Dream!"
print(s)
print(len(s))
print(s[len(s) - 1])

b_true = True
c_false = False

d_none = None

print(type(1))
print(type(1.2))
print(type(s))
print(type(b_true))
print(type(d_none))


# 运行模式【交互模式(输入一行、执行一行)、命令行模式(.py设计好内容，再一行一行地执行)】


# 输入模式【一律返回字符串类型】
# result = input("来点好玩的东西吧\n")
# print(result)
# print(int(result))
# print(float(result))
# print(str(result))
# height = float(input("身高输入"))/100
# weight = float(input("体重输入"))
# print("BMI: ", weight / (height ** 2))


# 条件判断
# mood_index = int(input("心情好不好呀，给打几分？\n"))
#
# if mood_index >= 1:
#     print("Great!")
# elif mood_index <= -1:
#     print("Good Night!")
# else:
#     print("Normal!")


# 多条件嵌套
# data = int(input("这次考试考了多少分呀？\n"))
# if data >= 0:
#     if data < 60:
#         print("没有及格呢！加油加油")
#     elif data < 70:
#         print("考得还不错，看看哪里不会")
#     elif data < 80:
#         print("这次真的还可以，要不，再努努力，也许就更好了！")
#     elif data < 90:
#         print("棒棒哒，我的宝！")
#     else:
#         print("您真牛！太棒啦！")
# else:
#     print("您这成绩是准备倒反天罡嘛？？")


# 逻辑运算【and,or,not】
# x = 10
# print(x > 5 and x < 10)
# print(x > 5 or x < 10)
# print(not x > 5)


# 列表【x.yy()：调用方法，x()：调用函数】
shopping_list = ["asd",2]

shopping_list.append("digger")
shopping_list.append("rusher")

print(shopping_list)
print(len(shopping_list))
print(shopping_list[2])

shopping_list[2] = "Russia"
print(shopping_list)

"""
max,min,sorted 等等列表函数，可以获得想要的结果
"""
data_list = [2,5,7,4,1,9,0,6]
max_value = max(data_list)
min_value = min(data_list)
sorted_list = sorted(data_list)

print(max_value)
print(min_value)
print(sorted_list)


# 字典