"""
案例：演示子类重写父类功能。

重写解释：
    概述：
        重写也叫覆盖，即：子类出现和父类重名的属性 或者 行为， 称之为：重写
    调用层次：
        遵循 就近原则， 子类有就调用， 没有就去就近的父类找，依次查找其所有的父类，有就用，没有就报错
"""

# 1. 师傅类
class Master:
    def __init__(self):
        self.kongfu = ['古法配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 2. 学校类
class School:
    def __init__(self):
        self.kongfu = ['新式配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 3. 徒弟类
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = ['独创配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 测试
if __name__ == '__main__':
    p = Prentice()
    p.make_cake()
    print(p.kongfu)