import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        self.power = 100    #初始体力

        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])      #随机初始位置

    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])       #随机选择方向和距离

        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x      #检查是否超出x轴边界(若超出则反方向移动)

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y      #检查是否超出y轴边界

        self.power -= 1

        return (self.x, self.y)      #返回移动后的位置

    def eat(self):
        self.power += 20        #吃掉鱼体力增加20
        if self.power > 100:
            self.power = 100    #体力上限100

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        new_x = self.x + r.choice([-1, 1])
        new_y = self.x + r.choice([-1, 1])

        if new_x < legal_x[0]:
            self.x = legal_x[0] + 1
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - 1
        else:
            self_x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] + 1
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - 1
        else:
            self_y = new_y

        return (self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼被吃完了，游戏结束！')
        break
    if not turtle.power:
        print('乌龟体力耗尽，游戏结束！')
        break

    pos = turtle.move()

    #在迭代器中删除列表元素很危险，经常出现意想不到的问题，因为迭代器直接引用列表数据进行引用
    #这里把列表拷贝给迭代器，然后对列表进行.remove就不会有问题
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print('一条鱼被吃掉了！')
