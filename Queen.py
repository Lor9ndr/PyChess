from ChessMan import *
from Empty import *


class Queen(ChessMan):
    IMG = ('♛', '♕')

    def GetMoves(self, board, x, y):
        # возможные движения королевы
        chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        intervals = chessCardinals + chessDiagonals
        moves = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.isInBounds(xtemp, ytemp):
                target = board.board[ytemp][xtemp]
                if isinstance(target, Empty):
                    moves.append((xtemp, ytemp))
                elif target.color != self.color:
                    moves.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return moves
