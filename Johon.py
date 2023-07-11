import random

def PlayGame():
    min=1
    max=50
    count=0
    target=random.randint(min,max)
    print("=======Guess number Game======\n\n")
    
    while(True):
        keyin=int(input(f"Guess number range{min}~{max}:"))
        count+=1
        
        if target==keyin:
            print(f"Correct!Answer is {target}")
            print(f"You use {count} times to guess it")
            break
        elif target<keyin:
            print("More smaller!")
            max=keyin-1
        elif target>keyin:
            print("More bigger!")
            min=keyin+1
        print(f"You guess{count} times to do it")
        
while(True):
    PlayGame()
    play_again=input("Do you want to play again?(y,n)")
    if not (play_again=='y'):
        break
print('GameOver')
            