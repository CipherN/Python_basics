#定义类
class Cat:

    #定义方法

    def __init__(self, new_name, new_age):
        print("----haha----")
        self.name = new_name
        self.age = new_age

    #def __str__(self):
        #return "%s的年龄是%d"%(self.name, self.age)

    def eat(self):
        print("猫正在吃鱼。。。")

    def drink(self):
        print("猫正在喝可乐。。。")

    def introduce(self):
        print("%s的年龄是%d"%(self.name, self.age))

tom = Cat("汤姆", 40)

#bluecat = Cat("蓝猫", 10)

print(tom)
#不使用__str__()方法的时候，直接打印对象，结果为该对象所在的内存地址
#使用__str__后打印可以输出所需要的“魔术”信息

bluecat = Cat("蓝猫", 10)

print(bluecat)
