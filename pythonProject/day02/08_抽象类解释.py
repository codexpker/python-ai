"""
案例：演示抽象类的用法。

抽象类解释：
    概述：
        在Python中，抽象类 = 接口，即：有抽象方法的类就是抽象类，也叫接口
        抽象方法 = 没有方法体的方法，即方法体是pass修饰的
    作用/目的：
        抽象类一般充当父类，用于指定行业规范，准则，具体的实现有子类实现
"""

# 定义抽象类
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

# 定义子类
class XiaoMi(AC):
    def cool_wind(self):
        print('xiaomi cool wind')
    def hot_wind(self):
        print('xiaomi hot wind')
    def swing_l_r(self):
        print('xiaomi swing l r')

class Green(AC):
    def cool_wind(self):
        print('green cool wind')
    def hot_wind(self):
        print('green hot wind')
    def swing_l_r(self):
        print('green swing l r')

# 测试
if __name__ == '__main__':
    xiaomi = XiaoMi()
    xiaomi.cool_wind()
    xiaomi.hot_wind()
    xiaomi.swing_l_r()
    print('-' * 32)
    green = Green()
    green.cool_wind()
    green.hot_wind()
    green.swing_l_r()

