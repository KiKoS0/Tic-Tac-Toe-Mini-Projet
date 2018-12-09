


import random

X = 'X'
O = 'O'
Empty = ' '

regles_vic = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

gameboard_conversion = {0:(0,0),1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}

def GetOpponent(car):
    if car is X: return O
    return X

def GetAvailableMoves(GameBoard):
    a=[Item for Item, Value in enumerate(GameBoard) if Value is Empty]
    return a


def ConvertGameBoard(GameBoard):
    newGameBoard = []
    for i in range(0, 3):
        for j in range(0, 3):
            newGameBoard.append(GameBoard[i, j].contenu)
    return newGameBoard

class MinMaxBot:
    def __init__(self):
        self.GameBoard = None
        self.pion = None
        self.Opponent = None
        self.GameEnded = False
        self.base_score = None

    def play(self, GameBoard, Char):
        # reinitialize this turn properties
        self.GameBoard = ConvertGameBoard(GameBoard)
        self.pion = Char
        self.Opponent = GetOpponent(Char)
        Least = -9999
        BestPlay = []
        self.base_score = len(GetAvailableMoves(self.GameBoard))
        if self.base_score is 9:
            return gameboard_conversion[4]
        for Move in GetAvailableMoves(self.GameBoard):
            self.select_case(Move, Char)
            Value = self.meilleur_coup(GetOpponent(Char), -(self.base_score + 1), self.base_score + 1, 0)
            self.select_case(Move, Empty)
            if Value > Least:
                Least = Value
                BestPlay = [Move]
            elif Value == Least:
                BestPlay.append(Move)
        return gameboard_conversion[random.choice(BestPlay)]

    def a_gagne(self):
        for Char in ('X', 'O'):
            Moves = [Move for Move, Value in enumerate(self.GameBoard) if Value == Char]
            for WinningState in regles_vic:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if Char is self.pion:
                        self.GameEnded = True
                        return self.pion
                    elif Char is self.Opponent:
                        self.GameEnded = True
                        return self.Opponent
        Items = len([Item for Item, Value in enumerate(self.GameBoard) if Value!=Empty])
        if Items is 9:
            self.GameEnded = True
            return 'Draw'
        return None


    def select_case(self, position, pion):
        self.GameBoard[position] = pion

    # this algorithm use minimax algorithm with alpha beta pruning
    def meilleur_coup(self, pion, lower_bound, upper_bound, depth=0):
        winner = self.a_gagne()
        if self.GameEnded:
            if winner is self.pion:
                return self.base_score-depth
            elif winner is self.Opponent:
                return depth-self.base_score
            elif winner is 'Draw':
                return 0
        for coup in GetAvailableMoves(self.GameBoard):
            self.select_case(coup, pion)
            Value = self.meilleur_coup(GetOpponent(pion), lower_bound, upper_bound, depth + 1)
            self.select_case(coup, Empty)
            if pion == self.pion:
                if Value > lower_bound:
                    lower_bound = Value
                if lower_bound >= upper_bound:
                    return upper_bound
            else:
                if Value < upper_bound:
                    upper_bound = Value
                if upper_bound <= lower_bound:
                    return lower_bound
        if pion == self.pion:
            return lower_bound
        else:
            return upper_bound
