class Person:

    def __init__(self, new_name, new_weight):

        self.name = new_name
        self.weight = new_weight

    def __str__(self):

        return "%s 爱跑步，体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货" % self.name)
        self.weight += 1


xm = Person("小明", 75.0)
xm.run()
xm.eat()
print(xm)

xmei = Person("小美", 45.0)
xmei.eat()
xmei.run()
print(xmei)
print(xm)
