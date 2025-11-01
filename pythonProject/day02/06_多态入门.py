"""
案例：演示多态入门

多态概述：
    专业：同一个函数在接受不同的函数有不同的效果
    大白话：同一个事物在不同时刻表现出来的不同状态，形态

    前提条件：
        1. 要有继承条件
        2. 要有方法重写，不然多态无意义
        3. 要有父类引用指向子类对象
    案例：
        动物类案例
"""

# 定义动物类
class Animal:   # 抽象类(也叫：接口)
    def speak(self):    # 抽象方法
        pass

# 定义子类
class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

# 定义函数，接受不同动物对象，调用speak方法
def make_noise(an:Animal):     #Java中 Animal an = Dog()
    an.speak()          #Python中 an:Animal = Dog()

# 测试
# dog:Animal = Dog() # 父类引用指向子类对象
# dog:Dog = Dog() # 创建够累对象
dog = Dog()
make_noise(dog)
print('-' * 34)
cat = Cat()
make_noise(cat)
print('-' * 34)


