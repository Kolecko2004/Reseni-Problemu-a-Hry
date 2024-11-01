import constant
import playerRND

class MyGame:
    def __init__(self, p1, p2, num_wins):
        self.p1 = p1
        self.p2 = p2
        self.num_wins = num_wins

    def draw (self):
        res1 = self.p1.select_move()
        res2 = self.p2.select_move()
        while (res1 == res2):
            res1 = self.p1.select_move()
            res2 = self.p2.select_move()
        print(res1, res2)
        if (res1, res2) in [('R','S'), ('P', 'R'), ('S','P')]:
            return (0, 1)
        else:
            return (1, 0)

    def run(self):
        scores = [0, 0]
        while max(scores) < self.num_wins:
            result = self.draw()

if __name__ == '__main__':
    p1 = playerRND.MyPlayer()
    p2 = constant.MyPlayer()
    game = MyGame(p1, p2, 3)
#    for i in range (10):
#        print(p.select_move())