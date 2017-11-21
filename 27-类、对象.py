#定义类
class Cat:

    #属性

    #方法
    def eat(self):
        print("猫正在吃鱼。。。")

    def drink(self):
        print("猫正在喝可乐。。。")

    def introduce(self):
        print("%s的年龄是%d"%(self.name, self.age))

#创建第一个对象，向内存申请一个空间
tom = Cat()

#调用Tom指向的对象中的方法
tom.eat()
tom.drink()

#给tom指向的对象添加属性
tom.name = "汤姆"
tom.age = 40

tom.introduce()

#创建第二个对象，向内存申请另一个空间
bluecat = Cat()

#给bluecat指向的对象添加属性
bluecat.name = "蓝猫"
bluecat.age = 10

bluecat.introduce()
