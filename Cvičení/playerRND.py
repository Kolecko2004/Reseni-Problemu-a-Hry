import random


class MyPlayer:
    def select_move(self):
        return random.choice(['R', 'P', 'S'])


if __name__ == '__main__':
    p = MyPlayer()
    for i in range(10):
        print(p.select_move())
