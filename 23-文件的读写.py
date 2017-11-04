"""文件的写入"""
f = open("hello world.py","w")

f.write("HELLO WORLD")

f.close()




"""文件的读取"""

f = open("hello world.py","r")  
"""open("hello world.py")"""  #python默认以只读的方式打开文件，所以可以不写 "r" 

content = f.read()

print(content)

f.close()
