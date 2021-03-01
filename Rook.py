from ChessMan import *


class Rook(ChessMan):
    IMG = ('♜', '♖',)
    moves_made = 0

    def GetMoves(self, board, x, y):
        # возможные движения ладьи

        moves = []
        for j in (-1, 1):
            i = x + j
            # Можем двигаться до тех пор пока не встретим элемент нашего цвета
            while 0 <= i <= 7:
                color = board.GetColor(i, y)
                if color == self.color:
                    break
                moves.append((i, y))
                if color != Color.EMPTY:
                    break
                i += j
        for j in (-1, 1):
            i = y + j
            # Можем двигаться до тех пор пока не встретим элемент нашего цвета
            while 0 <= i <= 7:
                color = board.GetColor(x, i)
                if color == self.color:
                    break
                moves.append((x, i))
                if color != Color.EMPTY:
                    break
                i += j

        return moves
