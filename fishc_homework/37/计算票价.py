#平日票价100
#周末120%
#儿童半票
#计算2a+1c

class Ticket:
    def __init__(self, weekend = False, child = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def calPrice(self, num):
        return self.exp * self.inc * self.discount * num

adult = Ticket()
child = Ticket(child = True)
print('2成人+1小孩平日票价为：%.2f' % (adult.calPrice(2) + child.calPrice(1)))
