"""
案例： 演示str魔法方法的用法

魔法方法：
    概述：
        Python的内置函数，在满足特定的场景下，会被 自动调用
    常用的魔法方法：
        __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
        __str__() 当用print()函数打印对象的时候，会自动调用该对象(所在类)的str魔法方法
        __del__() 当.py文件执行结束，或者手动 del 释放对象资源会自动调用该函数。
"""

# 1.定义汽车类， 属性：品牌， 行为run() 通过del魔法方法删除该类的对象，看看效果。
class Car:
    # 2.在魔法方法init中，完成：属性的初始化
    def __init__(self, brand):
        self.brand = brand
    # 3.重写魔法方法str，打印对象的属性值
    def __str__(self):
        return f'品牌：{self.brand}'
    # 4.重写del魔法方法，删除对象时给出提示
    def __del__(self):
        print(f'{self}对象被删除了')
    # 5. 定义run方法
    def run(self):
        print('run')

# 创建对象
c1 = Car('Ford')
print(c1)
del c1
print('-' * 32)
c2 = Car('Volvo')
print(c2)