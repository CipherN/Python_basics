'''列表定义方式:列表名字 = []
特别注意[]里面可以是整型，浮点型，也可以是字符串
'''

num = [1,2,3.14,"100","laowang"]

print(num[2])

'''列表增删改查
增加:append or insert or extend
name.append("添加元素")  #在最后添加
name.insert("位置下标，添加元素")  #指定位置添加
name.extend()  #最后添加

删除:pop or remove or 使用切片 or del name[下标]
name.pop()  #将最后元素取出并删除；
name.remove("元素")  #删除指定内容，重复内容只删除最左边的
name[2:5]  #切片出来的还是列表
del name[下标]  #删除指定下标

改：name[下标] = "新元素"

查询：in or not in 
for "元素" in name:
    print("在名单里面...")

for "元素" not in name:
    print("可以添加...")

#栈：后进先出，就像乘电梯，人快满的时候，最后上的人现出来

'''
