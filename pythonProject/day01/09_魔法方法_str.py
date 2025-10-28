"""
案例： 演示str魔法方法的用法

魔法方法：
    概述：
        Python的内置函数，在满足特定的场景下，会被 自动调用
    常用的魔法方法：
        __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
        __str__() 当用print()函数打印对象的时候，会自动调用该对象(所在类)的str魔法方法
        __del__()
"""

# 1.定义汽车类
class Car():
    # 2. 有参的 __init__()函数，参数值由：外部对象赋值
    def __init__(self, color, number):
        """
        该魔法方法用于给对象赋值
        :param color: 颜色
        :param number: 轮胎数
        """
        self.color = color
        self.number = number
    # 魔法方法 str(), 默认打印地址值，无意义，一般会重写，改为打印对象的各个属性值。
    def __str__(self):
        return f'颜色：{self.color}，对象：{self.number}'

c1 = Car('red', 7)
print(c1)