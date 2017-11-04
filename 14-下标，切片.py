name = "abcdefABCDEF"

'''其中下标从0开始计数，如a下标为0，b下标为1,f下标为5
从左向右下标为正，从右向左下标为负，如F下标为-1，D下标为-3
'''

print(name[0])
print(name[1])
print(name[5])

print(name[-1])
print(name[-3])  #下标注意点

'''
切片：从字符串中取出一段字符；
'''
print(name[2:5])#切片规则：name[起始下标:(终止下标+1)]

#取name中cdefABCDE

print(name[2:-1]) #E下标为-2！！！

print(name[2:]) #结束下标不填，表示取到最后一位字符

print(name[:]) #起始、结束下标都不填，全取name

print(name[2:5:2]) #name[起始下标:结束:步长]

print(name[::-1]) #倒序，步长可以为负值，表示从右向左取字符
