#-*- coding:utf-8 -*-
i = 1
while i <= 9:
   
    j = 1
    while j <= i:
        print("%d*%d=%d\t"%(j,i,j*i), end = "")#\t相当于tab键，用于对齐
        j += 1
        
    
    print("\n")#\n用于换行
    i += 1
