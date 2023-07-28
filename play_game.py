import random
def play_Games():
    min=1
    max=50
    count=0
    target=random.randint(1,50)
    print("========猜數字遊戲========\n\n")
    
    while True:
        count+=1
        keyin=int(input(f"請輸入其中一個數字{min,max}:\n"))
        if(keyin>=min and keyin<=max):
            if(keyin==target):
                if (count<=3):
                    print("哇靠!你居然這麼快就答對了!你是不是運氣上來了?")
                    print(f"你一共花了{count}次解決問題\n")
                    break
                else:
                    print(f"恭喜你答對了。\n你一共花了{count}次猜對。\n")
                    break
            elif(keyin<target):
                print("再大一點!\n")
                min=keyin
            elif(keyin>target):
                print('再小一點!\n')
                max=keyin
            print(f'你已經猜了{count}次\n')
        else:
            print("請輸入範圍內的字。")
            continue
while(True):
    play_Games()
    play_again=input('還要玩嗎(y,n)?')
    if play_again!="y":
        break
print("遊戲結束")