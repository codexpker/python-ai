"""
案例：继承入门

继承介绍：
    概述：
        大白话：子承父业
        专业：子类可以继承父类的属性和行为
    写法：
        class 子类名(父类名):
            pass
    例如：
        class A(B):
            pass
    叫法：
        A: 子类，派生类
        B: 父类， 基类
    好处：
        提高代码的复用性
    弊端：
        耦合性增强了，父类不好的内容，子类想没有都不行
    扩展：开发原则
        高内聚，低耦合
        内聚：指的是类自己独立处理问题的能力
        耦合：指的是类与类之间的关系
        大白话：自己能搞定的事，就不要麻烦别人
"""
# 需求定义父类(男，散步)，定义子类，继承父类。

# 定义父类
class Father(object):
    def __init__(self):
        self.gender = '男'
    def walk(self):
        print('walk...')
    def __str__(self):
        return f'gender: {self.gender}'
    # def smoke(self):
    #     print('smoke...')

# 定义子类
class Son(Father):
    pass

son = Son()
print(son)
son.walk()