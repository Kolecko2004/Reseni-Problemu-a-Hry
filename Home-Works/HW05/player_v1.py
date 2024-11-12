class MyPlayer:
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

        self.del_invalid_moves()  # double check if moves are all inside the game board
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

            self.main_cycle(x, y, 0)
            self.main_cycle(x, y, 1)
            self.main_cycle(x, y, 2)
            self.main_cycle(x, y, 3)

            self.main_cycle(x, y, 4)
            self.main_cycle(x, y, 5)
            self.main_cycle(x, y, 6)
            self.main_cycle(x, y, 7)

    def main_cycle(self, x, y, direction):
        # print(f'position {x}, {y}')
        x_pos = [1, 0, -1, 0, 1, -1, 1, -1]
        y_pos = [0, 1, 0, -1, -1, 1, 1, -1]
        x_size = x_pos[direction]
        y_size = y_pos[direction]

        points = 0

        while self.is_inside(x, y, x_pos, y_pos, x_size, y_size, direction):

            if self.board[x + x_size][y + y_size] == self.opponent_color:

                # print(f'{x + x_pos[direction] + x_size}, {y + y_pos[direction] + y_size}')

                points += 1
                if self.board[x + x_pos[direction] + x_size][y + y_pos[direction] + y_size] == self.void:
                    self.points_for_move.append(points)
                    return self.move.append((x + x_pos[direction] + x_size, y + y_pos[direction] + y_size))

                x_size += x_pos[direction]
                y_size += y_pos[direction]

            else:
                return

    def is_inside(self, x, y, x_pos, y_pos, x_size, y_size, direction):
        if -1 < x + x_pos[direction] + x_size < self.board_size and -1 < y + y_pos[direction] + y_size < self.board_size:
            return True
        else:
            return False

    def del_invalid_moves(self):
        index = 0
        for i in self.move:
            index += 1
            if index == len(self.move):
                return
            for s in i:
                if s < 0:
                    self.move.remove(i)


if __name__ == '__main__':
    c = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1,  0, -1, -1, -1],
        [-1, -1, -1,  0,  0, -1, -1, -1],
        [-1, -1, -1,  1,  0,  1, -1, -1],
        [-1, -1, -1, -1, -1,  0, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]

    p = MyPlayer(1, 0)
    print(p.select_move(c))
