import random

player = int(input("请输入0剪刀,1石头,2布:"))

computer = random.randint(0,2) 

if player == computer:
    
    print("平局，洗洗手继续玩...")

elif (player == 0 and computer == 1) or (player==1 and computer==2) or (player==2 and computer==0):

    print("输了，再玩一局？")

else:

    print("赢了，继续玩！")
