"""
案例：演示对象属性  和 类属性
属性介绍：
    概述：
        它是一个名词，用来描述事物的外在特征
    分类：
        对象属性：属于每个对象的，即：每个对象的属性值可能不同。 修改A对象属性，不影响B对象
        类属性：属于类的，即：能被该类下的所有对象所共享。   A对象修改类属性，B对象访问的是修改后的
    对象属性：
        定义到init魔法方法中的属性，每个对象都有自己的内容
        只能通过对象名的方式调用
    类属性：
        定义到类中，函数外的属性（变量），能被该类下所有的对象所共享
        既能通过 类名. 还能通过 对象名. 的方式来调用，推荐使用类名调用
"""

class  Student:
    # 类属性
    teacher_name = 'wang'
    # 对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '姓名： %s，年龄：%d' % (self.name, self.age)

# 测试
s1 = Student('zhangsan', 7)
s2 = Student('zhangsan', 7)

# 修改对象属性
s2.name = 'lisi'
s2.age = 9

print(s1)
print(s2)

print('-' * 32)

print(s1.teacher_name)
print(s2.teacher_name)
print(Student.teacher_name)
print('-' * 32)

# 尝试用 对象名. 的方式来修改类属性
# s1.teacher_name = 'zhangsan' # 只能给s1对象赋值，不能给类属性赋值

# 如果要修改变量的值，只能通过 类名. 的方式实现
Student.teacher_name = 'zhao'
print(s1.teacher_name)
print(s2.teacher_name)
print(Student.teacher_name)