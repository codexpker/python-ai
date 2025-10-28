"""
案例： 演示魔法方法 init 有参版，实际开发常用

回顾：__init__()魔法方法，在创建对象的时候，会被自动调用，一般用来给类对象的属性进行初始化
"""
# 1.定义汽车类
class Car:
    # 属性
    # 方法
    def __init__(self, color, number):
        """
        该魔法方法用于 给汽车类 对象的属性 赋值
        :param color: 车的颜色
        :param number: 轮胎数
        """
        self.color = color
        self.number = number
    def show(self):
        print(f'颜色：{self.color}，轮胎数： {self.number}')

# 创建对象
# c1 = Car() # 报错，因为创建对象的时候默认调用了init()函数，但是函数有参数，则必须传参
c1 = Car('red', 6)
c1.show()
print('-' * 34)

c2 = Car('blue', 7)
c2.show()

# ctrl + q 询问
c3 = Car()