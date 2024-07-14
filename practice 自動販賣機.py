#首先,創立菜單dict:
menu={
    "薯條":60,
    "可樂":30,
    "雞塊":50,
    "炸全雞":320,
    "葡式蛋塔":200,
    "雪碧":30,
    "烤雞":320
    }

print("菜單")
print("================")
#創造一個空list&total=0,會於加總計算與點菜數目中計算
cart=[]
total=0
#使用items()功能,讓點菜數量與價格可以在點餐後顯示出來
for item,price in menu.items():
    print(f'{item}:{price}')

while True:
    food=input(("請輸入想要點的菜(按q結束)"))
    if food =='q':
        break
    #使用get() is None方法來表明菜單中沒有所屬物件時的處理法
    elif menu.get(food) is None:
        print("沒有此商品!") 
    else:
        cart.append(food)
        #藉由total +=menu.get(food) 來相加所點字串中食物的價格
        total +=menu.get(food)
        

    print(f"你點了:{cart},總共:{total}元")