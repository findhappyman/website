import random
i = random.randint(1,10)
g=1
answer= 0 
while( answer != i and g <= 3):
    temp = input("请猜数(1~10):")
    answer = int(temp)
    if (answer > i):
        print("猜大了")
        g+=1
    elif (answer < i ):
        print("猜小了")
        g= g+1
    else:
        print("你猜对啦，真有默契")
if g > 3:
    print("四次机会你都没猜对，太遗憾了") 
