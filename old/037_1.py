import random
class Turtle:
    position = [random.randint(0,10),random.randint(0,10)]
    HP = 100
    def move(self):
        self.HP -= 1
        self.position[random.randint(0,1)] += random.choice([-2,-1,1,2])
        for i in range(0,2):
            if self.position[i] == 11:
                self.position[i] = 9
            elif self.position[i] == -1:
                self.position[i] = 1
            elif self.position[i] == -2:
                self.position[i] = 2
            elif self.position[i] == 12:
                self.position[i] = 8
        print('体力还剩下%d'% self.HP)
        print('当前龟的坐标是（%d,%d）。' % (self.position[0],self.position[1]))
    def eat(self):
        self.HP += 30
class Fish:
    position = {}
    position.fromkeys(range(1,11))
    for i in range(1, 11):
        position[i] = [random.randint(0, 10), random.randint(0, 10)]
    def move(self):
        for i in range(1,11):
            try:
                self.position[i][random.randint(0,1)] += random.choice([-1,1])
                for j in range(0,2):
                    if self.position[i][j] == 11:
                        self.position[i][j] = 9
                    elif self.position[i][j] == -1:
                        self.position[i][j] = 1
                print('当前鱼%d的坐标是（%d,%d）。' % (i,self.position[i][0], self.position[i][1]))
            except KeyError:
                pass
turtle = Turtle()
fish = Fish()
turtle.quantity = 1
fish.quantity = 10
while turtle.HP > 0 and fish.quantity > 0:
    try :
        turtle.move()
        fish.move()
        for i in range(1, 11):
            if turtle.position == fish.position[i]:
                turtle.eat()
                print('鱼%d被吃了！'% i)
                fish.quantity -=1
                del fish.position[i]
    except KeyError:
        pass
if turtle.HP == 0:
    turtle.quantity = 0
if turtle.quantity == 0:
    print('结果是龟死了，鱼还剩下%d' % fish.quantity)
else:
    print('结果是：\n龟活到了最后，鱼都被吃了')