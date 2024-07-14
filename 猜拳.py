#設定一個由random.choice()的方法執行猜拳遊戲
import random
#藉由設定Player and Computer = None 讓原始str為一個空str
Player=None
Computer=None
#可藉由設定Running = True 布林值變數,來決定某迴圈完成後是否再執行一次(方便迴圈執行)
Running=True
option=("剪刀","石頭","布")
while Running:
    print("歡迎遊玩猜拳遊戲!")
    Player=input("請輸入剪刀,石頭,布:")
    Computer=random.choice(option)

    while Player not in option:
        #請記住!如果玩家選擇選項並非選項中的內容,一定要打Player=input("內容");不然會困在迴圈中
        Player=input("輸入錯誤!請輸入剪刀,石頭,布!")
    
    print(f"玩家{Player},電腦{Computer}")

    if Player==Computer:
        print("平手!")

    elif Player=="剪刀" and Computer=='布':
        print("玩家勝利!(電腦:抱歉未能讓玩家盡興....)")
    elif Player=='布' and Computer=='石頭':   
        print("玩家勝利!(電腦:抱歉未能讓玩家盡興....)")
    elif Player=='石頭' and Computer=='剪刀':
        print("玩家勝利!(電腦:抱歉未能讓玩家盡興....)")
    else:
        print("電腦勝利!(玩家:未能讓電腦盡興.....)")
    
    play_again=input("再玩一局?(y/n)").lower()

    if not play_again=='y':
        print("遊戲結束!")
        Running=False