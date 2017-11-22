#定义类
class Cat:

    #定义方法

    def __init__(self, new_name, new_age):
        print("----haha----")
        self.name = new_name
        self.age = new_age
    
    def eat(self):
        print("猫正在吃鱼。。。")

    def drink(self):
        print("猫正在喝可乐。。。")

    def introduce(self):
        print("%s的年龄是%d"%(self.name, self.age))

tom = Cat("汤姆", 40)
tom.eat()
tom.drink()
tom.introduce()

bluecat = Cat("蓝猫", 10)
bluecat.eat()
bluecat.drink()
bluecat.introduce()

