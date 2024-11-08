class MyPlayer:
    '''Hráč hraje tak, aby získal co nejméně kamenů a aby byl v rozích a na stranách'''

    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.nobody = -1
        self.board_size = 8
        self.round_num = 0

    def move_corners(self):
        corners = [(0, 0), (7, 0), (0, 7), (7, 7)]

        for i in corners:
            if i in self.move:
                return i

    def move_sides(self):
        for move in self.move:
            x, y = move
            if x == 0 or x == self.board_size - 1 or y == 0 or y == self.board_size - 1:
                return move

    def bad_moves(self):
        bad_positions = [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6),
                         (1, 7), (6, 0), (6, 1), (7, 1), (6, 7), (6, 6), (7, 6)]
        bad_count = 0

        for i in bad_positions:
            if i in self.move:
                bad_count += 1

        if bad_count < len(self.move):
            for i in bad_positions:
                if i in self.move:
                    self.points_for_move.pop(self.move.index(i))
                    self.move.remove(i)

    def select_move(self, board):
        self.round_num += 1
        self.points_for_move = []
        self.move = []
        self.board = board

        self.find_positions()
        self.find_moves()
        self.del_invalid_moves()  # double check if moves are all possible
        self.bad_moves()
        # print(self.move, 'my moves')

        if len(self.move) == 0:
            return

        a = self.move_corners()
        if a != None:
            return a

        a = self.move_sides()
        if a != None:
            return a

        if self.round_num < 9:
            if not self.points_for_move:
                return None
            min_p_move = self.points_for_move.index(min(self.points_for_move))
            return self.move[min_p_move]

        else:
            if not self.points_for_move:
                return None
            max_p_move = self.points_for_move.index(max(self.points_for_move))
            return self.move[max_p_move]

    def find_positions(self):
        self.my_positions = []
        for position_y in range(self.board_size):
            for position_x in range(self.board_size):
                if self.board[position_x][position_y] == self.my_color:
                    self.my_positions.append(([position_x], [position_y]))

    def find_moves(self):
        for index in range(len(self.my_positions)):
            x = self.my_positions[index][0][0]
            y = self.my_positions[index][1][0]

            self.main_cycle(x, y, 0)  # right
            self.main_cycle(x, y, 1)  # down
            self.main_cycle(x, y, 2)  # left
            self.main_cycle(x, y, 3)  # up

            self.main_cycle(x, y, 4)  # right-up
            self.main_cycle(x, y, 5)  # left-down
            self.main_cycle(x, y, 6)  # right-down
            self.main_cycle(x, y, 7)  # left-up

    def main_cycle(self, x, y, direction):
        x_pos = [1, 0, -1, 0, 1, -1, 1, -1]
        y_pos = [0, 1, 0, -1, -1, 1, 1, -1]
        x_size = x_pos[direction]
        y_size = y_pos[direction]

        points = 0

        while self.is_inside(x, y, x_pos, y_pos, x_size, y_size, direction):

            if self.board[x + x_size][y + y_size] == self.opponent_color:
                # print(f'{x + x_pos[direction] + x_size}, {y + y_pos[direction] + y_size}')

                points += 1

                if self.board[x + x_pos[direction] + x_size][y + y_pos[direction] + y_size] == self.nobody:

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
                # print(i)
                if s < 0 or s >= self.board_size:
                    self.move.remove(i)
                if i is self.my_positions:
                    self.move.remove(i)
