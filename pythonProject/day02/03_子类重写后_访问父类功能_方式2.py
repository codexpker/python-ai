"""
案例：子类重写父类功能后，继续访问父类功能

思路：
    1. 父类名.父类函数名(self)  精准访问，想找哪个父类，就调用哪个父类。
    2. super().父类函数名()  只能访问最近的那个父类，有就用，没有就继续往后查找。
"""

# 1. 师傅类
class Master:
    # def __init__(self):
    #     self.kongfu = ['古法配方']
    # def make_cake(self):
    #     print(f'运用{self.kongfu}制作煎饼果子')
    pass
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
    # def make_master_cake(self):
    #     Master.__init__(self)
    #     Master.make_cake(self)
    # def make_school_cake(self):
    #     School.__init__(self)
    #     School.make_cake(self)
    def make_old_cake(self):
        super().__init__()
        super().make_cake()

# 测试
if __name__ == '__main__':
    p = Prentice()
    p.make_cake()
    print(p.kongfu)
    print('-' * 34)
    # p.make_school_cake()
    # p.make_master_cake()

    p.make_old_cake()
    print('-' * 34)
    p.make_cake()