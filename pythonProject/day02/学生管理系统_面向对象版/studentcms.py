"""
该文件用于 完成学生管理系统的 具体业务操作：即：增删改查，保存学生信息等
"""
# 导包
from student import Student
import time
# 1.创建学生管理系统类
class StudentCMS:
    # 2.魔法方法init，初始化属性信息
    def __init__(self):
        # 初始化一个空列表，用于存储学生对象
        self.stu_list = [
            # Student('芳华', '男', '24', '1533243211', '高中'),
            # Student('夏之光', '男', '24', '1831232111', '大学'),
            # Student('小孙', '女', '24', '1732132111', '同学')
        ]

    # 3.定义函数，用于打印 管理系统 信息
    @staticmethod
    def show():
        print('*' * 32)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')

    # 4.定义函数，实现添加学生信息功能
    def add_student(self):
        # 4.1 用户输入信息
        name = input("请输入要添加的姓名：")
        age = int(input("请输入要添加的年龄："))
        gender = input("请输入要添加的性别：")
        phone = input("请输入要添加的电话：")
        desc = input("请输入要添加的描述信息：")
        # 4.2 创建学生对象
        student = Student(name, age, gender, phone, desc)
        # 4.3 把学生对象添加到列表中
        self.stu_list.append(student)
        # 4.4 提示
        print(f'添加{name}学生信息成功！')
    # 5.定义函数，实现删除学生信息的功能
    def del_student(self):
        # 5.1 用户输入信息
        name = input('请输入要删除学生的姓名：')
        # 5.2 遍历用户列表，找到要删除的学生，并删除该学生信息
        for student in self.stu_list:
            # 5.3如果当前学生的姓名和要删除的学生相同，就删除该学生
            if student.name == name:
                self.stu_list.remove(student)
                # 提示
                print(f'删除学生{name}成功')
                break
        else:
            print(f'没有姓名为{name}的学生')
    # 6.定义函数，实现修改学生信息的功能
    def update_student(self):
        # 6.1 用户输入信息
        name = input('请输入要修改学生的姓名：')
        # 6.2 遍历用户列表，找到要修改的学生，并修改
        for student in self.stu_list:
            # 6.3 如果当前学生的姓名和要修改的学生相同，就修改该学生信息
            if student.name == name:
                # 6.4 提示用户录入该学员新的信息
                student.age = int(input("请输入要修改的年龄："))
                student.gender = input("请输入要修改的性别：")
                student.phone = input("请输入要修改的电话：")
                student.desc = input("请输入要修改的描述信息：")

                print(f'学生{name}信息修改成功\n')
                break
        else:
            # 查无此人
            print(f'没有姓名为{name}的学生\n')
    # 7.定义函数，实现查询单个学生信息的功能
    def search_one_student(self):
        # 7.1 用户输入信息
        name = input('请输入要查询学生的姓名：')
        # 7.2 遍历列表，找到要查找的学生， 并打印信息。
        for student in self.stu_list:
            # 7.3 如果当前学生的姓名 和 要查找的学生相同，就打印该学生信息
            if student.name == name:
                print(student, end='\n\n')
                break
        else:
            # 查无此人
            print(f'没有姓名为{name}的学生')
    # 8.定义函数，实现查询所有学生信息的功能
    def search_all_student(self):
        # 8.1 判断列表长度是否为0,如果为0,提示暂无学生信息
        if(len(self.stu_list) == 0):
            print('暂无学生信息,请稍后查询!\n')
        # 8.2 如果长度不为0,遍历列表，打印出所有的学生信息
        else:
            for student in self.stu_list:
                print(student)
            print() #为了格式好看
    # 9.定义函数，实现保存学生信息的功能
    def save_student(self):
        # 9.1 关联学生信息文件
        with open('./stu_data.txt', 'w', encoding='utf-8') as f:
            # 9.2 把[学生对象，学生对象...] -> [字典，字典...]
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            # 9.3 把字典列表持久化到文件中
            f.write((str(stu_dict))) #接的转成字符串再写入
    # 10.定义函数，用于加载学生信息
    def load_student(self):
        # 10.1 加入异常处理机制，文件可能不存在
        try:
            # 10.2 关联 学生信息文件
            with open('./stu_data.txt', 'r', encoding='utf-8') as f:
                # 10.3 一次性读取所有数据
                stu_data = f.read() #'[字典，字典...]‘
                # 10.4 把字符串转链表
                stu_dict = eval(stu_data)
                # 10.5 判断如果列表为空，就赋予空列表
                if(len(stu_dict) == 0):
                    self.stu_list = []
                else:
                    # 10.6 把列表中的字典封装成学生对象,并赋值给 self.stu_list
                    self.stu_list = [Student(**stu) for stu in stu_dict]
        except:
            # 10.7 目的文件不存在，创建即可
            with open('./stu_data.txt', 'w', encoding='utf-8') as f:
                pass
    # 11.定义函数，把上述业务逻辑跑通
    def start(self):
        # 11.1 加载学生信息
        self.load_student()
        # 11.2 死循环
        while True:
            # 11.3 为了效果更明显，加入延时机制
            time.sleep(1)
            # 11.4 打印 学生管理系统界面
            StudentCMS.show()
            # 11.5 提示用户录入要操作的编号，并接收
            input_num = input('请输入您要操作的编号: ')
            if input_num == '1':
                self.add_student()
            elif input_num == '2':
                self.del_student()
            elif input_num == '3':
                self.update_student()
            elif input_num == '4':
                self.search_one_student()
            elif input_num == '5':
                self.search_all_student()
            elif input_num == '6':
                self.save_student()
                print('保存信息成功！\n')
            elif input_num == '0':
                # 退出系统，做二次校验
                result = input('您确定要退出系统吗？ （Y/N）： ')
                if result.lower() == 'y': # 字符串的lower() =>把字母转成小写形式
                    # 退出前，自动保存学生数据到文件
                    self.save_student()
                    print('谢谢你的使用，期待下次再会！\n')
                    break
            else:
                # 输入错误
                print('录入有误，请重新录入！\n')

# 12.测试
if __name__ == '__main__':
    cms = StudentCMS()
    cms.start()

    # # 打印当前路径
    # import os
    # print(os.getcwd())