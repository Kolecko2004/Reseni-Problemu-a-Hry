import random


class MyPlayer:
    '''Player that returns moves randomly as True or False.'''

    def __init__(self, payoff_matrix, number_of_iterations=20):
        self.payoff_matrix = payoff_matrix
        self.iteNum = number_of_iterations
        self.i = 0
        self.opp_moves = []

    def get_vector(self):
        return self.payoff_matrix

    def select_move(self):
        self.i += 1
        # Randomly choose True or False for each move
        return random.choice([True, False])
    # return random.choice([True, False])

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_move = my_last_move
        self.opponent_move = opponent_last_move
        self.opp_moves.append(opponent_last_move)
