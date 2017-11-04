#获取用户输入的三个值
num1 = int(input("第一个值:"))
num2 = int(input("第二个值:"))
num3 = int(input("第三个值:"))

def sum(a, b, c):
    result = a+b+c
    print("%d+%d+%d=%d"%(num1,num2,num3,result))
#sum(num1, num2, num3)
    return result

def average(d,e,f):
    result2 = sum(num1,num2,num3)
    result2/=3
    print("平均值为:%d"%result2)
#average(num1,num2,num3)
    return result2

def squre(g,h,i):
    result3 = average(num1,num2,num3)
    result3 = result3**2
    print("平方:%d"%result3)
squre(num1,num2,num3)
