# 程序测试
import unittest
from test import add
from test import Sentence


# 面向对象编程【创建对象，包括属性、方法】
"""
封装：只需要调用方法名，便能够实现想执行的过程

继承：允许继承类，并获得所有上层的属性、方法
class person
class student(person)

多态：不同子类的同名方法，可以有不同的实现效果
"""

# 创建类
# 类继承
"""
类命名：使用pascal方法，单词首字母大写
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"""我的名字是{self.name},今年{self.age}岁,很高兴见到你！""")

    def change_age(self, new_age):
        self.age = new_age


class Student(Person):
    def __init__(self, name, age, number, chinese, math, english):
        super().__init__(name, age)
        self.number = number
        self.chinese = chinese
        self.math = math
        self.english = english
        self.average = format((self.chinese + self.math + self.english) / 3, ".2f")

    def print_info_student(self):
        print(
            f"""我的名字是{self.name},今年{self.age}岁,很高兴见到你！\n我的学号是{self.number},这次考试,\n我的语文成绩是{self.chinese},数学成绩是{self.math},英语成绩是{self.english}\n平均分是{self.average}""")


a = Person("瓦拉卡", 32)
a.print_info()
a.change_age(20)
a.print_info()

b = Student("布鲁克斯", 16, "A00312", 66.7, 72.5, 96)
b.print_info_student()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"""姓名:{self.name},工号:{self.id}""")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        print(f"""我是全职员工{self.name},我的月薪是:{self.monthly_salary}""")

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary,work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        print(f"""我是兼职员工{self.name},我的月薪是:{self.daily_salary * self.work_days}""")

worker1 = FullTimeEmployee("复方","A001",2300)
worker2 = PartTimeEmployee("赖简析","CF001",120,6)

worker1.calculate_monthly_pay()
worker2.calculate_monthly_pay()


# 文件路径【绝对路径、相对路径】
# 读取文件【调用(需要关闭文件，释放资源)、函数体】

f = open("./files/data.txt","r",encoding="utf-8")
print(f.read(20))
print(f.readline())
print(f.read())
f.close()

with open("./files/data.txt","r",encoding="utf-8") as f:
    print(f.read())


# 文件写入【w表示写入内容,a表示追加内容,r+表示追加内容与读取内容】

# with open("./files/data_write.txt", "w",encoding="utf-8") as f:
#     f.write("Hello!\n")
#     f.write("Bulubulu!\n")
#
# with open("./files/data_write.txt", "a",encoding="utf-8") as f:
#     f.write("Loving!\n")
#     f.write("we will be here.")


# 异常处理【索引错误、除零错误、找不到文件、类型错误等等】

# try:
#     data = input("请输入一个数字:")
#     print(f"""这个数字的五次方 = {int(data) ** 5}""")
# except ValueError:
#     print("输入的内容不是数字，请重新运行程序。")
# except:
#     print("发生了未知错误")
# else:
#     print("程序运行正常")
# finally:
#     print("程序运行结束")


# 程序测试【assert,unittest】

# assert len("abc") == 3
# assert 1+2>6

"""
运行指令：
python -m unittest [文件地址]
"""
class TestMyAdder(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(1,2), 3)

    def test_add_2(self):
        self.assertEqual(add(1, 2), 5)

    def test_add_3(self):
        self.assertTrue(add(1,2), 3)

    def test_add_4(self):
        self.assertIn(add(1, 2), [2,3,4,5])

    def test_add_5(self):
        self.assertNotEqual(add(1,2), add(1,2))

    def test_add_6(self):
        self.assertFalse(add(1,2) == 2)

    def test_add_7(self):
        self.assertNotIn(add(1,2), [2,3])

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("You cannot improve your past,but you can improve your future.Once time is wasted,life is wasted.Don't aim for success if you want it;just do what you love and believe in,and it will come naturally.")

    def test_sentence(self):
        self.assertEqual(self.sentence.length(),26)


# 高阶和匿名函数【传入函数，而不是调用函数的结果】
"""
高阶函数：传入函数进行使用
匿名函数：lambda 参数1,参数2: 参数表达式【会直接返回结果】
"""