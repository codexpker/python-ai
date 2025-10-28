"""
案例：小明当前体重是100kg。每当他跑步一次，则会减少0.5kg；每当他大吃一顿时，则会增加2kg。
分析：
    类名： Student
    对象名：xm
    属性： 体重，weight
    行为：跑步，吃饭
"""
# 1.定义同学对象
class Student:
    # 2.在魔法方法init中，完成对象的初始化
    def __init__(self, weight):
        self.weight = weight

    # 3. 每当跑步依次，则会减少0.5kg
    def run(self):
        self.weight -= 0.5
    # 4. 大吃大喝一顿，增加2kg
    def eat(self):
        self.weight += 2
    # 5.重写魔法方法str，打印属性值，即：当前体重。
    def __str__(self):
        return f'体重：{self.weight}kg'

# 6.测试
if __name__ == '__main__':
    # 6.1 创建对象
    xm = Student(100)
    # 6.2 跑步
    xm.run()
    xm.run()
    print(xm)
    # 6.3 吃喝
    xm.eat()
    print(xm)