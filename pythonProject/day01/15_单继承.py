"""
案例：演示单继承，即，1个子类继承1个父类
分析：
    1. 定义师傅类， Master
        属性：kongfu
        行为：make_cake()
    2. 定义子类， Prentice，继承师傅类
"""

class Master:
    def __init__(self):
        self.kongfu = '[古法配方]'
    def make_cake(self):
        print(f'采用{self.kongfu}摊煎饼')

class Prentice(Master):
    pass

p = Prentice()
p.make_cake()