
print("名单管理系统")
print("="*12)
print("1.添加姓名")
print("2.删除姓名")
print("3.更改姓名")
print("4.查找姓名")
print("5.退出系统")
print("="*12)

names = []

while True:

    name =int(input("请输入操作序号："))

    if name == 1:
        
        add_name =input("请输入添加的姓名：")

        names.append(add_name)
        
        print(names)

    elif name == 2:
      
        del_name = input("请输入删除的姓名：") 
        
        names.remove(del_name)

        print(names)

    elif name == 3:
        
        print(names)
        
        name1 = input("请输入需修改的姓名：")

        while True:

            if name1 not in names:
                
                print("查无此人")
                break
            else:

                name2 = input("请输入修改后的姓名：")
                
                a = int(names.index(name1))

                names[a] = name2

                print(names)
                break
    elif name == 4:
        
        find_name = input("请输入查找的姓名：")

        if find_name in names:
            print("在名单里。")
        else:
            print("查无此人！")



    elif name == 5:
       
        break

    else:
        print("输入有误，请重新输入：")
       
        break
