import random
import easygui as g

a = random.randint(1,10)
countnum = 0

while countnum < 5:
    guess =g.integerbox(msg= '不妨猜一下小甲鱼现在心里想的是哪个数字（1-10），你有五次机会。',title= '数字小游戏',lowerbound = 1,upperbound = 10)
    if guess == a:
        print('猜对啦！')
        break
    elif guess > a :
        print('猜大了！')
        countnum +=1
    else:
        print('猜小了！')
        countnum +=1
if countnum >=5:
    print('五次机会用完啦！')
print('欢迎再来玩')
