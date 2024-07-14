import random
dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

#設定投出色子顆數
num_dice=int(input("請問要擲幾顆骰子?"))
#藉由設定空字串dice=[],來讓下面的dice.append(dice_number)以list方法秀出擲骰結果
dice=[]
for i in range(num_dice):
    dice_number=random.randint(1,6)
    dice.append(dice_number)
print(dice)

#自建def get_dice_number(number)方法來讓結果正常顯示出dice_art的圖片
def get_dice_number(number):
    # range(5)--指dice_art中的五個組成骰子圖的圖片
    for i in range(5):
        print(dice_art.get(number)[i])
#以此迴圈來結合前面的dice所得數字結果,並以get_dice_number(i)來結合for i in range(num_dice)
#後的結果數字
for i in dice:
    get_dice_number(i)
print("總和為:",sum(dice))


#然我對這裡的def自建方法方式尚有不能通透之地,需要找到相關書籍與加強基本邏輯,方能完全正確理解
#可擴充,並變成猜色子大小遊戲

