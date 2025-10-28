"""
需求：定义一个手机类，能开机，能关机，可以拍照
"""

# 1.定义手机类
class Phone:
    # 1.1 开机
    def open(self):
        print(f'open:{self}')
    # 1.2 关机
    def close(self):
        print(f'close:{self}')
    # 1.3 拍照
    def take_photo(self):
        print(f'take photo:{self}')

# 2.创建对象
p1 = Phone()
print(f'p1对象:{p1}')
p1.open()
p1.take_photo()
p1.close()
print('-' * 30)

# 3.继续创建对象
p2 = Phone()
print(f'p2对象：{p2}')
p2.open()
p2.take_photo()
p2.close()