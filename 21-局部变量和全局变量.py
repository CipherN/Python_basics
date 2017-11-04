#局部变量：意思就是函数里面定义的变量，另外一个函数无法调用，函数外面的print等也无法调用，示例如下：
def test1():
    a = 100

def test2():
    print("a=%d"%a)

test1()

#test2()

#print("a=%d"%a)

#无论是调用test2还是在test1函数外面打印a的值，均会报错 a is not defined

#全局变量：意思就是函数外面定义的变量，无论在函数定义前还是函数调用前，示例如下：
a = 100
def test3():
    print(a)#a的变量定义在函数定义前，调用函数test3可以打印出来

def test4():
    print(b)#b的变量定义在函数定义后，调用函数test4可以打印出来

b = 200

test3()
test4()
