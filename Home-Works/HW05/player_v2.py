class MyPlayer:
    '''Hráč hraje tak, aby získal co nejméně kamenů a aby byl v rozích a na stranách'''

    def __init__(self, my_color, opponent_color):
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.nobody = -1
        self.board_size = 8
        self.round_num = 0

    def pick_corner_move(moves):
        corners = [(0, 0), (7, 0), (0, 7), (7, 7)]

        for i in corners:
            
            
            if i in moves:
                return i

    def pick_border_move(self, moves):
        for move in moves:
            x, y = move
            if x == 0 or x == self.board_size - 1 or y == 0 or y == self.board_size - 1:
                return move

    def rid_of_bad_moves(self):
        bad_positions = [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6),
                        (1, 7), (6, 0), (6, 1), (7, 1), (6, 7), (6, 6), (7, 6)]
        bad_count = 0

        for i in bad_positions:
            if i in self.all_poss_moves:
                bad_count += 1

        if bad_count < len(self.all_poss_moves):
            for i in bad_positions:
                if i in self.all_poss_moves:
                    self.points_for_move.pop(self.all_poss_moves.index(i))
                    self.all_poss_moves.remove(i)

    def select_move(self, board):
        self.round_num += 1
        self.points_for_move = []
        self.all_poss_moves = []
        self.board = board

        self.find_positions()
        self.find_moves(self.all_poss_moves)
        self.del_invalid_moves()  # double check if moves are all possible
        self.rid_of_bad_moves()
        # print(self.all_poss_moves, 'my moves')

        if len(self.all_poss_moves) == 0:
            return

        result = self.pick_corner_move(self.all_poss_moves)
        if result != None:
            return result

        result = self.ahead_move()
        if result != None:
            return result

        result = self.pick_border_move(self.all_poss_moves)
        if result != None:
            return result

        if self.round_num < 20:
            if not self.points_for_move:
                return None
            min_p_move = self.points_for_move.index(min(self.points_for_move))
            return self.all_poss_moves[min_p_move]

        else:
            if not self.points_for_move:
                return None
            max_p_move = self.points_for_move.index(max(self.points_for_move))
            return self.all_poss_moves[max_p_move]

    def find_positions(self):
        self.my_positions = []
        for position_y in range(self.board_size):
            for position_x in range(self.board_size):
                if self.board[position_x][position_y] == self.my_color:
                    self.my_positions.append(([position_x], [position_y]))

    def find_moves(self, moves):
        for index in range(len(self.my_positions)):
            x = self.my_positions[index][0][0]
            y = self.my_positions[index][1][0]

            moves.append(self.main_cycle(x, y, 0))  # right
            moves.append(self.main_cycle(x, y, 1))  # down
            moves.append(self.main_cycle(x, y, 2))  # left
            moves.append(self.main_cycle(x, y, 3))  # up

            moves.append(self.main_cycle(x, y, 4))  # right-up
            moves.append(self.main_cycle(x, y, 5))  # left-down
            moves.append(self.main_cycle(x, y, 6))  # right-down
            moves.append(self.main_cycle(x, y, 7))  # left-up

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
                    return (x + x_pos[direction] + x_size, y + y_pos[direction] + y_size)
                    #return self.all_poss_moves.append((x + x_pos[direction] + x_size, y + y_pos[direction] + y_size))
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
        for i in self.all_poss_moves:
            index += 1
            if index == len(self.all_poss_moves):
                return
            for s in i:
                # print(i)
                if s < 0 or s >= self.board_size:
                    self.all_poss_moves.remove(i)
                if i is self.my_positions:
                    self.all_poss_moves.remove(i)

    def ahead_move(self):
        self.all_poss_new_moves = []
        for i in self.all_poss_moves:
            self.play_move(i)
            self.find_positions()
            self.find_moves(self.all_poss_new_moves)
            result = self.pick_corner_move(self.all_poss_new_moves)
            if result != None:
                return i

            result = self.pick_border_move(self.all_poss_new_moves)
            if result != None:
                return i

    def play_move(self, move):
        self.board[move[0]][move[1]] = self.my_color

        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        for i in range(len(dx)):
            if self.confirm_direction(move, dx[i], dy[i]):
                self.change_stones_in_direction(
                    move, dx[i], dy[i])

    def confirm_direction(self, move, dx, dy):
        opponents_color = self.opponent_color

        posx = move[0]+dx
        posy = move[1]+dy
        if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
            if self.board[posx][posy] == opponents_color:
                while (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                    posx += dx
                    posy += dy
                    if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                        if self.board[posx][posy] == self.nobody:
                            return False
                        if self.board[posx][posy] == self.my_color:
                            return True

        return False

    def change_stones_in_direction(self, move, dx, dy):
        posx = move[0]+dx
        posy = move[1]+dy
        while (not (self.board[posx][posy] == self.my_color)):
            self.board[posx][posy] = self.my_color
            posx += dx
            posy += dy


if __name__ == "__main__":
    c = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1,  0,  1, -1, -1, -1],
        [-1, -1, -1,  0,  0, -1, -1, -1],
        [-1, -1, -1,  1,  0,  1, -1, -1],
        [-1, -1, -1, -1, -1,  0, -1, -1],
        [-1, -1, -1, -1, -1, -1,  0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]

    p = MyPlayer(1, 0)
    print(p.select_move(c))
