from Color import *


class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def enemy_color(self):
        return Color.invert(self.color)

    def GetMoves(self, board, x, y):
        return ()

    def __repr__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]

    @staticmethod
    def isInBounds(x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        return False
