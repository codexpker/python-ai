"""
案例：演示Python多态案例：战斗平台
需求：
    1.构建对战平台(公共的函数) object_play(), 接收：英雄机 和 敌机
    2. 在不修改代码的情况下，完成多次战斗。
    3. 规则：英雄机：1代战斗力60 2代战斗力80
            敌机：战斗力70
分析：
    公共函数(英雄机，敌机)

总结：
    封装：
        好处：安全性，复用性
        弊端：代码量增加
    继承：
        好处：复用性，子承父业
        弊端：耦合性增强
    多态：
        好处；应用解耦（同函数接收不同参数有不同结果）
        弊端：无法精准限定类型
    Python中：抽象类等于接口
"""
# 定义抽象类
class HeroFighter(object):
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
    
class EnemyFighter(object):
    def attack(self):
        return 70

# 构建对战平台，公共函数，接收不同的参数，有不同的效果 -> 多态
def object_play(herofighter: HeroFighter, enemyfighter: EnemyFighter):
    if herofighter.power() >= enemyfighter.attack():
        print('英雄战机胜利')
    else:
        print('英雄战机失败')
f1 = HeroFighter()
f2 = AdvHeroFighter()
enemy = EnemyFighter()
# 思路1：不使用多态
if f1.power() >= enemy.attack():
    print('英雄战机胜利')
else:
    print('英雄战机失败')
if f2.power() >= enemy.attack():
    print('英雄战机胜利')
else:
    print('英雄战机失败')

print('-' * 34)
# 思路2： 使用多态

object_play(f1, enemy)
object_play(f2, enemy)