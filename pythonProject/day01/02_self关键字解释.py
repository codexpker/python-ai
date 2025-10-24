"""
案例： self关键字介绍

self介绍：
    概述：
        它是python内置的关键字，用于表示 本类当前对象的引用。
    作用：
        1个类是可以有多个对象的，这多个对象都可以通过 对象名. 的方式访问类中的行为（函数）
        函数默认有self属性，通过self来区分具体调用的是哪个函数
    大白话：
        谁调用 self就代表谁
"""
from symtable import Class

# 定义汽车类
class Car:
    def run(self):
        print("run---")
        print(f"run: {self}")

# 创建对象
c1 = Car()
print(f'c1对象: {c1}')
print(f'c1地址：{id(c1)}')

# Car#run()
c1.run()

print("-" * 30)


# 再次创建对象
c2 = Car()
print(f'c2对象：{c2}')

# Car#run()
c2.run()