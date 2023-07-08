import random

min=1
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
    else:
        print("wrong")
        print(f"you use {count} times to guess")
print("fin")