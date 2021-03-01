from Color import *


class Empty(object):
    color = Color.EMPTY

    def GetMoves(self, board, x, y):
        return ()

    def __str__(self):
        return '. '
