class Test:
    def __init__(self,name='test',age=12):
        self.name = name
        self.age = age
    def p(self):
        self.age += 1
t = Test()
print(t.name,t.age)