"""
1. 使用面向对象、字符串、列表、字典、文件等知识点完成学生管理系统的开发
2. 针对学生，该系统具有添加、修改、删除、查询所有学生、查询某个学生、保存信息、退出系统等操作

需求：
    a.可以显示基本的版本信息和操作界面
    b.可以通过键盘输入信息来完成基本功能
    c.学生属性信息有：姓名、性别、年龄、联系方式、描述信息等
    d.使用系统可以对学生信息进行CRUD操作
    e.可以使用文件对学生信息进行加载、保存等
    f.可重复对学生信息进行CRUD操作，当确认退出系统后，则直接退出系统
    g.请使用面向对象的编程思想完成项目的升级处理
"""
# 定义学生类
class Student:
    def __init__(self, name, gender, age, phone, desc):
        """
        定义魔法方法，初始化属性
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        :param phone: 电话号码
        :param desc: 描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        定义魔法方法，用于打印学生信息
        :return:
        """
        return f'姓名：{self.name}，性别：{self.gender}，年龄：{self.age}，手机号：{self.phone}，描述信息：{self.desc}'

# 测试

if __name__ == '__main__':
    s1 = Student('zhangsan', '男',18, '14232353253','111')
    s2 = Student('lisi', '男',12, '2321443534','123')
    print(s1)
    print(s2)
