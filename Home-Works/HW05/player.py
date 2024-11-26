from copy import deepcopy


class MyPlayer:
    '''My player wants to be in corners and on the sides'''

    def __init__(self, my_color, opp_color):
        self.my_color = my_color
        self.opp_color = opp_color
        self.nobody_field = -1
        self.board_size = 8
        self.round = 0

    def pick_corner_move(self, poss_moves):
        field_corners = [(0, 0), (self.board_size - 1, 0), (0,
                                                            self.board_size - 1), (self.board_size - 1, self.board_size - 1)]

        for corner in field_corners:
            if corner in poss_moves:
                return corner

    def is_border(self, x_pos, y_pos):
        if x_pos == 0 or x_pos == self.board_size - 1 or y_pos == 0 or y_pos == self.board_size - 1:
            return True
        return False

    def pick_border_move(self, poss_moves):
        for move in poss_moves:
            x_pos, y_pos = move
            if self.is_border(x_pos, y_pos):
                return move

    def erase_bad_moves(self):
        # bad positions are those that give opponent chance to get into a corner or border
        worst_positions = [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6),
                           (1, 7), (6, 0), (6, 1), (7, 1), (6, 7), (6, 6), (7, 6)]
        bad_moves_count = 0
        worst_moves_count = 0

        for pos_move in self.my_poss_moves:
            x, y = pos_move
            if x == 1 or x == self.board_size - 2 or y == 1 or y == self.board_size - 2:
                bad_moves_count += 1
            if pos_move in worst_positions:
                worst_moves_count += 1

        if worst_moves_count < len(self.my_poss_moves):
            for worst_pos in worst_positions:
                if worst_pos in self.my_poss_moves:
                    self.delete_move(worst_pos)

        if bad_moves_count < len(self.my_poss_moves):
            for move in self.my_poss_moves:
                x, y = move
                if x == 1 or x == self.board_size - 2 or y == 1 or y == self.board_size - 2:
                    self.delete_move(move)

    def select_move(self, board):
        self.round += 1
        self.points_for_my_move = []
        self.my_poss_moves = []
        self.my_postions = []
        self.board = deepcopy(board)
        self.find_positions(self.my_postions, self.my_color, self.board)
        self.find_moves(self.my_poss_moves, self.points_for_my_move,
                        self.my_postions, self.board, self.opp_color)
        self.idx_depth_ahead = 0

        if len(self.my_poss_moves) == 0:
            return

        result = self.pick_corner_move(self.my_poss_moves)
        if result != None:
            return result

        result = self.pick_border_move(self.my_poss_moves)
        if result != None:
            return result

        self.erase_bad_moves()
        self.del_moves_opp_corner()

        result = self.ahead_move(self.my_poss_moves)
        if result != None:
            return result

        if self.round < 15:
            min_p_move = self.points_for_my_move.index(
                min(self.points_for_my_move))
            return self.my_poss_moves[min_p_move]

        else:
            max_p_move = self.points_for_my_move.index(
                max(self.points_for_my_move))
            return self.my_poss_moves[max_p_move]

    def find_positions(self, positions, color, board):
        for position_y in range(self.board_size):
            for position_x in range(self.board_size):
                if board[position_x][position_y] == color:
                    positions.append(([position_x], [position_y]))

    def find_moves(self, moves, points_arr, positions, board, opp_color):
        for index in range(len(positions)):
            x = positions[index][0][0]
            y = positions[index][1][0]

            self.main_cycle(x, y, 0, moves, points_arr,
                            board, opp_color)  # right
            self.main_cycle(x, y, 1, moves, points_arr,
                            board, opp_color)  # down
            self.main_cycle(x, y, 2, moves, points_arr,
                            board, opp_color)  # left
            self.main_cycle(x, y, 3, moves, points_arr, board, opp_color)  # up

            self.main_cycle(x, y, 4, moves, points_arr,
                            board, opp_color)  # right-up
            self.main_cycle(x, y, 5, moves, points_arr,
                            board, opp_color)  # left-down
            self.main_cycle(x, y, 6, moves, points_arr,
                            board, opp_color)  # right-down
            self.main_cycle(x, y, 7, moves, points_arr,
                            board, opp_color)  # left-up

    def main_cycle(self, x, y, direction, moves, points_arr, board, opp_color):
        x_pos = [1, 0, -1, 0, 1, -1, 1, -1]
        y_pos = [0, 1, 0, -1, -1, 1, 1, -1]
        x_size = x_pos[direction]
        y_size = y_pos[direction]

        points = 0

        while self.is_inside(x, y, x_pos, y_pos, x_size, y_size, direction):

            if board[x + x_size][y + y_size] == opp_color:
                # print(f'{x + x_pos[direction] + x_size}, {y + y_pos[direction] + y_size}')

                points += 1

                if board[x + x_pos[direction] + x_size][y + y_pos[direction] + y_size] == self.nobody_field:

                    points_arr.append(points)
                    return moves.append((x + x_pos[direction] + x_size, y + y_pos[direction] + y_size))
                    # return self.my_poss_moves.append((x + x_pos[direction] + x_size, y + y_pos[direction] + y_size))
                x_size += x_pos[direction]
                y_size += y_pos[direction]
            else:
                return

    def is_inside(self, x, y, x_pos, y_pos, x_size, y_size, direction):
        if -1 < x + x_pos[direction] + x_size < self.board_size and -1 < y + y_pos[direction] + y_size < self.board_size:
            return True
        return False

    def ahead_move(self, poss_moves):
        ahead_board = self.board
        for move in poss_moves:
            points_moves_ahead = []
            self.all_poss_new_moves = []
            my_positions_ahead = []
            self.play_move(move, ahead_board)
            self.find_positions(my_positions_ahead, self.my_color, ahead_board)
            self.find_moves(self.all_poss_new_moves, points_moves_ahead,
                            my_positions_ahead, ahead_board, self.opp_color)

            result = self.pick_corner_move(self.all_poss_new_moves)
            if result != None:
                return move

            result = self.pick_border_move(self.all_poss_new_moves)
            if result != None:
                return move

    def play_move(self, move, board):
        board[move[0]][move[1]] = self.my_color

        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        for i in range(len(dx)):
            if self.confirm_direction(move, dx[i], dy[i], board):
                self.change_stones_in_direction(
                    move, dx[i], dy[i], board)

    def confirm_direction(self, move, dx, dy, board):
        opponents_color = self.opp_color

        posx = move[0]+dx
        posy = move[1]+dy
        if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
            if board[posx][posy] == opponents_color:
                while (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                    posx += dx
                    posy += dy
                    if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                        if board[posx][posy] == self.nobody_field:
                            return False
                        if board[posx][posy] == self.my_color:
                            return True

        return False

    def change_stones_in_direction(self, move, dx, dy, board):
        posx = move[0]+dx
        posy = move[1]+dy
        while (not (board[posx][posy] == self.my_color)):
            board[posx][posy] = self.my_color
            posx += dx
            posy += dy

    def del_moves_opp_corner(self):
        for move in self.my_poss_moves:
            opp_positions = []
            board = self.board
            opp_moves = []
            opp_points = []
            self.play_move(move, board)
            self.find_positions(opp_positions, self.opp_color, board)
            self.find_moves(opp_moves, opp_points,
                            opp_positions, board, self.my_color)
            if self.pick_corner_move(opp_moves) != None and len(self.my_poss_moves) >= 2:
                self.delete_move(move)

    def delete_move(self, move):
        self.points_for_my_move.pop(self.my_poss_moves.index(move))
        self.my_poss_moves.remove(move)
