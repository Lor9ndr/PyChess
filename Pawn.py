from ChessMan import *
from Color import *


class Pawn(ChessMan):
    IMG = ('♟', '♙')

    def GetMoves(self, board, x, y):
        # возможные передвижения пешки
        moves = []
        y += -1 if self.color == Color.WHITE else 1
        if y == -1 or y == 8:
            return moves
        if x > 0 and board.GetColor(x - 1, y) == self.enemy_color():
            moves.append((x - 1, y))
        if x < 7 and board.GetColor(x + 1, y) == self.enemy_color():
            moves.append((x + 1, y))
        if board.IsEmpty(x, y):
            moves.append((x, y))
            if self.color == Color.WHITE and y == 5 and board.IsEmpty(x, y - 1):
                moves.append((x, y - 1))
            if self.color == Color.BLACK and y == 2 and board.IsEmpty(x, y + 1):
                moves.append((x, y + 1))
        return moves
