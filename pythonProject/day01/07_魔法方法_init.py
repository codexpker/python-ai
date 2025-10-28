"""
案例： 演示init魔法方法的用法

魔法方法：
    概述：
        Python的内置函数，在满足特定的场景下，会被 自动调用
    常用的魔法方法：
        __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
        __str__()
        __del__()
"""
# 需求： 定义汽车类，默认属性为：color = ’黑色’, number = 3

# 1. 定义汽车类
class Car:
    def __init__(self):
        print('我是 无参init 魔法方法')
        self.color = '黑色'
        self.number = 4
    def show(self):
        print(f"颜色：{self.color}，轮胎数{self.number}")

# 2. 创建对象
c1 = Car()
# 打印c1对象的属性值。
c1.number = 6
c1.color = '红色'
print(c1.color, c1.number)
c1.show()

print('-' * 34)
c2 = Car()
c2.show()