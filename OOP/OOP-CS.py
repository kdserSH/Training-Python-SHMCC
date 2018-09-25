#实例可以修改实例变量，不能修改类变量，程序调用时优先寻找实例变量，其次再找类变量。


class role(object):   #定义类
    n = 123 #类变量
    def __init__(self,name,role,weapon,life_value=100,money=15000):#构造函数，init是传参数用的，用于调用方法时传参数。
        self.name=name #实例变量
        self.role=role
        self.weapon=weapon
        self.life_value=life_value
        self.money=money
    def get_shot(self): #类的方法、功能
        print('Oh no,%s got shot'%self.name)
    def shot(self):
        print('%s Shooting'%self.name)
    def buygun(self,gun_name):
        print('%s got %s'%(self.name,gun_name))

r1=role('gsj','police','m4a')#类的实例化（aka初始化一个类）
r2=role('ddd','terroist','ak47')

r1.buygun('ak47')
r2.get_shot()
print(role.n)
r1.name='ak47'
r2.name='m4a'
r1.bulletproof=True

print(r1.bulletproof)
print(r1.n,r1.name)
print(r2.n,r2.name)


