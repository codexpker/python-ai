"""
案例：演示类内如何获取对象的属性

细节：
    类内如何设置属性，要结合 魔法方法 __init__() 来实现
"""

# 1. 定义汽车类，创建该对象，赋予颜色和轮胎两个属性，并在类内访问该属性

class Car:
    # 属性
    # 行为
    # 1.1 跑
    def run(self):
        print("汽车会跑")
    # 1.2 定义show()，实现 在类内访问属性
    def show(self):
        print(f'我是show函数，对象的颜色：{self.color},轮胎数：{self.number}')

# 2.创建汽车类的对象
c1 = Car()

# 3.给其赋予属性 -> 类外
c1.color = "red"
c1.number = 4

# 4.类外访问属性
print(f"c1:color:{c1.color},number:{c1.number}")

# 5.类外访问行为
c1.run()
c1.show()
print('-' * 34)

# 6.继续创建汽车类对象，尝试分别调用run(),show()
c2 = Car()
c2.run()
c2.show()



