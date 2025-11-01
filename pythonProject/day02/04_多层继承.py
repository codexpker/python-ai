"""
案例： 演示多层继承
多层继承解释：
    类A继承类B，类B继承类C，这就是多层继承
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
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
# 4. 徒孙类
class TuSun(Prentice):
    pass

# 测试
if __name__ == '__main__':
    ts = TuSun()
    ts.make_cake()
    ts.make_master_cake()
    ts.make_school_cake()