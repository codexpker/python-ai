"""
案例：演示类方法和静态方法
类方法：
    属于类的方法，可以通过类名. 还可以通过对象名.的方式调用
    定义类方法的时候，必须使用装饰器 @classmethod，且第一个参数必须表示 类对象
静态方法：
    属于该类下所有对象共享的方法，可以通过类名，还可以通过对象名.的方式来调用
    定义静态方法的时候，必须使用装饰器 @staticmethod，且参数传不传都可以
区别：
    1. 类方法的第1个参数必须是类对象，静态方法无参数的特殊要求
    2. 你可以理解为：如果函数中要使用 类对象，就定义类方法，否则就定义为静态方法，除此之外无任何区别
"""

class Student:
    age = 18

    # 定义类方法
    @classmethod
    def show1(cls):
        print(f'cls:{cls}') #cls:<class '__main__.Student'>
        print(cls.age)
        print('我是类方法')

    # 定义静态方法
    @staticmethod
    def show2():
        print('我是静态方法')

# 测试
s = Student()
s.show1()
s.show2()