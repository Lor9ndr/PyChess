from ChessMan import ChessMan
from Empty import Empty


class Bishop(ChessMan):
    IMG = ('♝', '♗')

    def GetMoves(self, board, x, y):
        # возможные движения слона
        # движение по диагоналям пока не встретим объект нашего цвета
        chess_diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        moves = []
        for x_int, y_int in chess_diagonals:
            x_temp, y_temp = x + x_int, y + y_int
            while self.isInBounds(x_temp, y_temp):
                target = board.board[y_temp][x_temp]
                if isinstance(target, Empty):
                    moves.append((x_temp, y_temp))
                elif target.color != self.color:
                    moves.append((x_temp, y_temp))
                    break
                else:
                    break
                x_temp, y_temp = x_temp + x_int, y_temp + y_int
        return moves