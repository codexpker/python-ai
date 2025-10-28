"""
案例： 演示通过self关键字， 在类内访问其他函数

# 需求：定义汽车类，类内用run()函数，并在work()中调用run()函数，创建该类对象，调用上述函数。

总结：
    1. 在 类外 访问类中的行为，需要通过 对象名. 的方式访问
    2. 在 类内 访问类中的行为，需要通过 self. 的方式访问
"""

# 1.定义汽车类
class Car:
    # 1.1 run()函数
    def run(self):
        print(f'{self} 汽车在跑---')
    # 1.2 work()函数，在其内部调用run()
    def work(self):
        print(f'我是work函数，我的self值是：{self}')
        self.run()

# 2.创建对象
c1 = Car()
print(f'c1对象：{c1}')
c1.run()
print('-' * 30)
c1.work()
print('=' * 30)


# 3. 再次创建对象
c2 = Car()
print(f'c2对象：{c2}')
c2.run()
print('-' * 30)
c2.work()