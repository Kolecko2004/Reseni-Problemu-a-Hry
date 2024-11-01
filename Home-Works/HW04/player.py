import random

class MyPlayer:
    '''Opakuje tahy druhého hráče + výběr strategie + drobnosti'''
    def __init__(self, payoff_matrix, number_of_iterations = None):
        self.payoff_matrix = payoff_matrix
        self.iteNum = number_of_iterations
        self.i = 0
        self.opp_moves = []
        self.true = 0
        self.false = 0
        
        self.strategy = 0
        a = self.payoff_matrix[0][0][0] * 2
        b = self.payoff_matrix[0][1][0] + self.payoff_matrix[1][0][0]
        c = self.payoff_matrix[1][1][0] * 2
        
        if self.payoff_matrix[0][0][0] > self.payoff_matrix[1][0][0] and self.payoff_matrix[0][0][0] > self.payoff_matrix[1][1][0]: # spoluprace je nejlepsi vzdy
            self.strategy = 2

        elif a > b and a > c: # nejlepsi je spoluprace - tit for tat
            self.strategy = 0

        elif b > a and b > c: # nejlepsi je podvádět
            self.strategy = 3

        elif c > a and c > b: # nejlepsi je kdyz oba podvadime
            self.strategy = 1

    def select_move(self):
        self.i += 1

        if self.strategy == 0:
            return self.strategy_0()

        if self.strategy == 1:
            return self.strategy_1()
        
        if self.strategy == 2:
            return self.strategy_2()
        
        if self.strategy == 3:
            return self.strategy_3()
        
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_move = my_last_move
        self.opponent_move = opponent_last_move
        self.opp_moves.append(opponent_last_move)
            
    def strategy_0(self):
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
        
    def strategy_1(self): # Pokud je pro oba dva výhodnější neustále DEFECT
        return True
    
    def strategy_2(self): # Pokud je pro oba dva výhodnější neustále COOPERATE
        return False
    
    def strategy_3(self): # Výhodné je ho DEFECT když on COOPERATE
        if self.i == 1: return True

        elif self.iteNum == self.i:
            return True

        elif self.i > 5 and all(move == self.opp_moves[0] for move in self.opp_moves[:self.i]):
            return True
        
        elif self.opponent_move == True:
            return True
        
        elif self.opponent_move == False:
            answer = random.choices([True, False], [6, 4])[0]
            return answer

if __name__ == '__main__':
    
    payoff_matrix = ( ((4,4),(1,6)) , ((6,1),(2,2)) )

    playerA = MyPlayer(payoff_matrix)
    print("Hello")

    print(playerA.select_move())