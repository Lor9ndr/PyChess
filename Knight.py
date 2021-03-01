from ChessMan import ChessMan


class Knight(ChessMan):
    IMG = ("♞", "♘")

    @staticmethod
    def knightList(x, y, int1, int2):
        """specifically for the rook, permutes the values needed around a position for noConflict tests"""
        return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
                (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]

    def GetMoves(self, board, x, y):
        return [(xx, yy) for xx, yy in self.knightList(x, y, 2, 1) if self.noConflict(board.board, xx, yy)]

    def noConflict(self, board, x, y):
        if self.isInBounds(x, y) and board[y][x].color != self.color:
            return True
        return False
