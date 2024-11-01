import random

class MyPlayer:
    '''Opakuje tahy druhého hráče + drobnosti'''
    def __init__(self, payoff_matrix, number_of_iterations = None):
        self.payoff_matrix = payoff_matrix
        self.iteNum = number_of_iterations
        self.i = 0
        self.opp_moves = []
        self.true = 0
        self.false = 0

    def get_vector(self):            
        return(self.payoff_matrix)
    
    def select_move(self):
        self.i += 1

        if self.i == 1: return False

        elif self.iteNum == self.i:
                return True

        elif self.i > 5 and all(move == self.opp_moves[0] for move in self.opp_moves[:self.i]):
            return True
        
        elif self.opponent_move == True:
            answer = random.choices([True, False], [9, 1])[0]
            return answer
        
        elif self.opponent_move == False:
                return False
        
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_move = my_last_move
        self.opponent_move = opponent_last_move
        self.opp_moves.append(opponent_last_move)