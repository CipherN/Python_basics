import os

#1.获取用户需要重命名文件对应的文件夹名

folder_name = input("请输入需要重命名文件的文件夹名字：")

#2.读取文件夹中文件的名字

file_names = os.listdir(folder_name)

##os.chdir(folder_name)  #一定要在用户制定文件夹中重命名，不然报错not found file or direction......

#3.重新命名文件
for name in file_names:


   # print(name)  调试读取是否正常
#第11行代码可以删除改写为下列两行：
    old_file_name = folder_name + "/" + name

    ### new_file_name = folder_name + "/" + "[youku]-" + old_file_name
    ###错误写法！只有单独命名new_file_name,即加上路径和命名规则，不可以使用old_file_name，正确写法如下：

    new_file_name = folder_name + "/" + "[youku]-" + name
    
    ##new_name = "[优酷出品]-" + name
   
    ##os.rename(name,new_name)

    os.rename(old_file_name, new_file_name)

