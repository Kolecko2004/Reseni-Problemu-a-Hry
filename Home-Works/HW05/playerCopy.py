class MyPlayers12:
    '''Hráč hraje tak, aby získal co nejméně kamenů a aby byl v rozích a na stranách'''

    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.void = -1
        self.board_size = 8
        self.move = []
        self.points_for_move = []

    def move_corners(self):
        corners = [(0, 0), (7, 0), (0, 7), (7, 7)]

        for i in corners:
            if i in self.move:
                return i

    def move_sides(self):
        index = 0
        for i in self.move:
            index += 1
            if index == len(self.move):
                return
            for s in i:
                if s == 0 or s == 7:
                    return i
                index = 0

    def select_move(self, board):
        self.board = board
        self.positions()
        self.find_moves()

        self.invalid_moves()
        # print(self.move)
        if len(self.move) == 0:
            return

        a = self.move_corners()
        if a != None:
            return a

        a = self.move_sides()
        if a != None:
            return a

        idk = self.points_for_move.index(min(self.points_for_move))
        return self.move[idk]

    def positions(self):
        self.my_positions = []
        for position_y in range(self.board_size):
            for position_x in range(self.board_size):
                if self.board[position_x][position_y] == self.my_color:
                    self.my_positions.append(([position_x], [position_y]))

    def find_moves(self):
        for index in range(len(self.my_positions)):
            # print("My positions:", self.my_positions[index][0][0], ',', self.my_positions[index][1][0])
            x = self.my_positions[index][0][0]
            y = self.my_positions[index][1][0]

            self.main_cycle(x, y, True, False, False, False)
            self.main_cycle(x, y, False, True, False, False)
            self.main_cycle(x, y, False, False, True, False)
            self.main_cycle(x, y, False, False, False, True)

            self.main_cycle(x, y, False, True, True, False)
            self.main_cycle(x, y, False, True, False, True)
            self.main_cycle(x, y, True, False, False, True)
            self.main_cycle(x, y, True, False, True, False)

    def invalid_moves(self):
        index = 0
        for i in self.move:
            index += 1
            if index == len(self.move):
                return
            for s in i:
                if s < 0:
                    self.move.remove(i)

    def main_cycle(self, x, y, down, up, left, right):
        # print(f'position {x}, {y}')
        index_down = 0
        down_add = 0
        index_up = 0
        up_add = 0
        indey_left = 0
        left_add = 0
        indey_right = 0
        right_add = 0

        points = 0
        if down == True:
            index_down += 1
            down_add = 1
        if up == True:
            index_up -= 1
            up_add = -1
        if left == True:
            indey_left -= 1
            left_add = -1
        if right == True:
            indey_right += 1
            right_add = 1

        while -1 < x + index_up + up_add + index_down + down_add < self.board_size and -1 < y + indey_left + left_add + indey_right + right_add < self.board_size:

            if self.board[x + index_up + index_down][y + indey_left + indey_right] == self.opponent_color:

                # print(f'{x + index_up + up_add + index_down + down_add}, {y + indey_left + left_add + indey_right + right_add}')

                points += 1
                if self.board[x + index_up + up_add + index_down + down_add][y + indey_left + left_add + indey_right + right_add] == self.void:
                    self.points_for_move.append(points)
                    return self.move.append((x + index_up + up_add + index_down + down_add, y + indey_left + left_add + indey_right + right_add))

                if down == True:
                    index_down += 1
                if up == True:
                    index_up -= 1
                if left == True:
                    indey_left -= 1
                if right == True:
                    indey_right += 1

            else:
                return


if __name__ == '__main__':
    c = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1,  0, -1, -1, -1],
        [-1, -1, -1, -1,  1, -1, -1, -1],
        [-1, -1, -1, -1,  0, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]

    p = MyPlayers12(1, 0)
    print(p.select_move(c))
