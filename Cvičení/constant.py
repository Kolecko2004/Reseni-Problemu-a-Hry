class MyPlayer:
    def select_move(self):
        return 'R'

if __name__ == '__main__':
    p = MyPlayer()
    for i in range (10):
        print(p.select_move()) 