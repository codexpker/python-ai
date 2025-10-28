"""
案例：演示多继承

扩展：MRO机制
    解释
        Python中由MRO机制，可以查看某个对象在调用函数的顺序，即，先找哪个类再找哪个类
    格式
        类名.mro()
        类名.__mro__
"""

# 1. 定义师傅类
class Master:
    def __init__(self):
        self.kongfu = ['古法配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 2. 定义学校类
class School:
    def __init__(self):
        self.kongfu = ['新式配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 3. 定义徒弟类
class Prentice(School, Master): # 从左往右，就近原则
    pass

# 定义对象
xm = Prentice()
print(xm.kongfu)
xm.make_cake()

print('-' * 34)

# 查看mro机制的返回结果
print(Prentice.mro()) # Prentice -> School -> Master
print(Prentice.__mro__) # Prentice -> School -> Master