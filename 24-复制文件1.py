"""文件内容复制"""
f = open("文件.py","w")

f.write("HELLO WORLD")

f.close()

f = open("文件.py","r")

content = f.read()

g = open("文件[副本].py","w")

g.write(content)

f.close()

g.close()


