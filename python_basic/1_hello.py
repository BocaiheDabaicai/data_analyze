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


# 字典【键值对("key":"value")，但不能将列表作为键，元组可以作为键，数据可变】
# 元组【值(value,value)，元组不可变】
contract = {"a":213132213,("a","b"):325645}
print(contract["a"])
print(contract[("a","b")])
print("a" in contract)
del contract["a"]
print(contract)

books = {"读文科":"阿斯顿的机会vu",
         "萨拉就":"法和恐惧的还是",
         "苏坡桥":"超级卡刷卡上车",
         "旗舰店":"来看电视剧啊离",}
print(books)
print(len(books))


# for循环【for 变量名 in 可迭代对象】
for_array = [234.3,242,233.4,544.343,234.324,21789.7,86]
for_tuple = ("askdl","dsakl","ckldsvvv")
for_dict = {"sdq":3212,"fsdf":95984,"vkjj":76778}

for item in for_array:
    print(item)

print("--------")
for item in for_tuple:
    print(item)

print("--------")
for item in for_dict:
    print(item)
print("--------")
for item,val in for_dict.items():
    print(item," ",val)
print("--------")
for item in for_dict.items():
    print(item[0]," ",item[1])

print("--------")
for item in range(0,5):
    print(item)
print("--------")
for item in range(0,5,2):
    print(item)
print("")

# while循环【while 条件:】
i=0
while i<100:
    i += 1
print(i)

# val = ""
# accumulate_list = []
# accumulate_sum = 0
#
# while val != "quit":
#     val = input("输入值吧: ")
#     if val == "quit":
#         break
#     else:
#         accumulate_list.append(float(val))
#
# for item in accumulate_list:
#     accumulate_sum += item
# print(accumulate_sum/len(accumulate_list))


# 格式化字符串【format方式, f""字符串方式】
string_content = """
{0}年大吉，天天开心。
快乐永存，祈福共天。
祝{1}天天快乐，幸福永存
""".format("虎","小明")

print(string_content)

string_content = """
{animal}年大吉，天天开心。
快乐永存，祈福共天。
祝{name}天天快乐，幸福永存
""".format(animal="兔",name="小吉祥")

print(string_content)

animal = "蛇"
name = "小静"

string_content = f"""
{animal}年大吉，天天开心。
快乐永存，祈福共天。
祝{name}天天快乐，幸福永存
"""

print(string_content)


# 函数
def calculate_sector(central_angle, radius):
    area =  central_angle / 360 * math.pi * radius ** 2
    print(f"该扇形的面积为:{format(area,'.2f')}")

def calculate_sector_return(central_angle, radius):
    area =  central_angle / 360 * math.pi * radius ** 2
    print(f"该扇形的面积为:{format(area,'.2f')}")
    return format(area,'.2f')

calculate_sector(44,2)
calculate_sector(89,2)
calculate_sector(77,2)

def get_data():
    data = 1
    while data <10:
        data += 1
    return data

def get_data_none():
    data = 1
    while data <10:
        data += 1

print(get_data())
print(get_data_none())

def BMI_calculate(weight, height):
    result = weight / (height * height)
    if result <= 18.5:
        print("偏瘦啦")
    elif result <= 25:
        print("很正常")
    elif result <= 30:
        print("偏胖")
    else:
        print("肥胖")

    return format(result,'.2f')

print(BMI_calculate(37,1.74))
print(BMI_calculate(68,1.75))
print(BMI_calculate(90,1.78))
print(BMI_calculate(190,1.74))


# 引入模块