"""1.输入要复制的文件名"""
old_file_name = input("请输入需要复制的文件名：")

"""2.打开文件(旧文件)"""
old_file = open(old_file_name,"r")


"""2.新文件文件名处理"""
"""[复件]文件名.py的实现方式"""
#new_file_name = "[复件]" + old_file_name

"""文件名[复件].py的实现方式"""
position = old_file_name.rfind(".")

new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

"""3.打开文件(新文件)"""
new_file = open(new_file_name,"w")

"""4.复制旧文件内容，写入新文件"""
content = old_file.read()
new_file.write(content)

"""5.关闭旧文件，新文件"""
old_file.close()
new_file.close()



