"""
案例： 演示封装之私有属性

封装简介：
    概述：
        属于去面向对象的三大特征之一，就是隐藏对象的属性和实现细节，仅对外提供公共的访问方式
    怎么封装？
        我们学习的函数和类都是封装的一种方式
    好处：
        1. 提高代码的安全性     由 私有化 保证
        2. 提高代码的复用性     由 函数 保证
    弊端：
        代码量增加，因为私有内容外界想访问，必须提供公共的访问方式，代码量就增加了
私有格式：
    __属性名
    __函数名()
"""

# 故事5： 小明把技术给徒孙时，不希望把自己的私房钱给徒孙，代码模拟

# 1. 定义师傅类 Master

# 2. 定义学校类 School

# 3. 定义徒弟类 Prentice

class Prentice:
    # 定义属性
    def __init__(self):
        self.kongfu = '[独创秘方]'
        self.__money = 10000
    ## 定义方法
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')
    ## 针对私有属性，提供公共的访问方式。
    def get_money(self):    # 获取
        return self.__money
    def set_money(self, money):     # 设置
        self.__money = money
# 4. 定义徒孙类
class TuSun(Prentice):
    pass

# 5. 测试
if __name__ == '__main__':
    ts = TuSun()
    print(ts.kongfu)
    ts.make_cake()
    print('-' * 34)
    # print(ts.money) # 报错，父类私有成员，子类无法访问
    ts.set_money(100)
    print(ts.get_money()) # 通过父类的公共访问方式，访问私有成员