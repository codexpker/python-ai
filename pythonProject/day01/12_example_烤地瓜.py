"""
案例：烤地瓜
分析：
    类：SweetPotato
    属性：时间 cook_time, 状态：cook_state, 调料：condiments
    行为：烤 cook(), 添加调料 add_condiments()
    魔法方法：init() -> 初始化属性，   str() -> 打印地瓜信息
    规则：
        烘烤时间    地瓜状态
        [0,3)       生的
        [3,7)       半生不熟的
        [7,12)      熟了
        [12,♾️)     烤糊了
"""

# 定义地瓜类
class SweetPotato:
    # 初始化属性
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []
    # 具体烘烤动作
    def cook(self, time):
        if time <= 0:
            print('无效值')
        else:
            # 根据烘烤时间，修改烘烤的状态
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state = '半生不熟的'
            elif 7 <= self.cook_time < 12:
                self.cook_state = '熟了'
            else:
                self.cook_state = '烤糊了'
    # 添加调料
    def add_condiments(self, condiment):
        self.condiments.append(condiment)
    # 重写 str()， 打印地瓜信息
    def __str__(self):
        return f'cook_state: {self.cook_state}, condiments: {self.condiments}， cook_time: {self.cook_time}'

# 测试
if __name__ == '__main__':
    # 创建地瓜对象
    digua1 = SweetPotato()
    print(digua1)
    # 具体的烘烤动作
    digua1.cook(3)
    # 添加调料
    digua1.add_condiments('辣椒')
    # 打印地瓜信息
    print(digua1)
    digua1.cook(5)
    digua1.add_condiments('酱油')
    print(digua1)

