class Dog:
    def __init__(self,name):
        self.name=name

    def bulk(self):
        print('%s,Wang!Wang!Wang'%self.name)


d1=Dog('snoopy')
d1.bulk()