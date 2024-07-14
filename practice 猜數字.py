import random


print("遊戲開始!")
running=True
low=1
high=100
number=random.randint(low,high)
time=0
while running:
    
    num=int(input(f"請猜一個從{low}~{high}的一個數字:"))
    time+=1
#使用low=num and high=num讓所猜數字次數可以減少
    if num<number:
        print("你猜的數字太小了!再大一點!")
        low=num
        continue

    elif num>number:
        print("你猜的數字太大了!再小一點!")
        high=num
        continue
    
    elif num==number:
        print(f"恭喜你猜中了!答案是{number},共用了{time}次")
        break

    elif time>10:
        print(f"遊戲結束!你失敗了,答案是{number}")
        break


print("遊戲結束!")