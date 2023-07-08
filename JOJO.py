import random

def playGame():
    min=0
    max=10
    count=0
    target=random.randint(min,max)

    while(True):
        keyin=int(input(f"猜數字範圍{min}~{max}:"))
        count+=1
        if(keyin==target):
            print(f"correct,answer is {target}")
            print(f"you use {count} times to guess")
            break
        elif keyin>target:
            print("more smaller!")
            max-=1
        elif keyin<target:
            print("more bigger!")
        min+=1
        print(f"you use {count} times to guess")
    print("fin")

while(True):
    playGame()
    Game_input=input("Do you want to play again?(y,n)")
    if not(Game_input=='y'):
        break
print("gameover")

