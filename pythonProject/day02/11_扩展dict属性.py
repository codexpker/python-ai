"""
案例：演示Python内置的dict属性

__dict__属性介绍：
    它是Python的内置属性，可以把对象转成字典形式
"""
# 导包
from 学生管理系统_面向对象版.student import Student

# 需求1：把学生对象 -> 字典形式
s1 = Student('zhangsan', '男', 18, '14232353253', '111')
dict_s1 = s1.__dict__
print(dict_s1)
print(type(dict_s1))
print('-' * 24)

# 需求2：把[学生对象，学生对象，学生对象] -> [字典，字典，字典]
s1 = Student('芳华', '男', '24', '1533243211', '高中')
s2 = Student('夏之光', '男', '24', '1831232111', '大学')
s3 = Student('小孙', '女', '24', '1732132111', '同学')
stu_list = [s1, s2, s3]
# 列表推导式
print([stu.__dict__ for stu in stu_list])
print('-' * 24)

# 需求3：把字典形式 -> 学生对象
s2 = Student(**dict_s1)
print(s2)
print(type(s2))
print('-' * 24)