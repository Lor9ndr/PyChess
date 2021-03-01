from Queen import Queen

from Bishop import Bishop
from King import *
from Empty import *
from Knight import Knight
from Pawn import *
from Rook import *


class ChessBoard(object):
    def __init__(self):
        self.board = [[Empty()] * 8 for _ in range(8)]
        self.history = []

    def GetColor(self, x, y):
        # Возвращает цвет объекта
        return self.board[y][x].color

    def GetMoves(self, x, y):
        return self.board[y][x].GetMoves(self, x, y)

    def GetChessman(self, x, y):
        # Функция возвращает элемен на координатах (x,y)
        return self.board[y][x]

    def GetChessmanMoves(self, x, y):
        # Функция возвращает список ходов по элементу на координатах (x,y)
        return self.GetChessman(x, y).GetMoves(self, x, y)

    def IsEmpty(self, x, y):
        # Проверка на пустую ячейку
        return self.GetChessman(x, y).color == Color.EMPTY

    def CanTransform(self, x, y) -> bool:
        # Проверка на возможнность трансформации
        obj = self.GetChessman(x, y)
        if obj.color == Color.WHITE and y == 0 and isinstance(obj, Pawn):
            return True
        if obj.color == Color.BLACK and y == 7 and isinstance(obj, Pawn):
            return True
        return False

    def MoveChessman(self, xy_from, xy_to):
        # Функция передвижения
        captured = self.board[xy_to[1]][xy_to[0]]
        if isinstance(self.board[xy_from[1]][xy_from[0]], Rook):
            self.board[xy_from[1]][xy_from[0]].moves_made +=1
        if isinstance(self.board[xy_from[1]][xy_from[0]], King):
            king: King = self.board[xy_from[1]][xy_from[0]]
            if king.moves_made == 0 and xy_to in king.castlingCoords.keys():
                self.MoveChessman(king.castlingCoords[xy_to],
                                  (xy_from[0] + king.GetRookSide(self, xy_from[0], xy_from[1]), xy_from[1]))
            self.board[xy_from[1]][xy_from[0]].moves_made += 1
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]

        self.board[xy_from[1]][xy_from[0]] = Empty()

        return captured

    def Transform(self, x, y):
        # трансформация из пешки в другой элемент
        try:
            inp = int(input("Введите 0 для того, чтобы не траснформироваться\n"
                            "Введите 1 для того, чтобы трансформироваться в ладью\n"
                            "Введите 2 для того, чтобы трансформироваться в коня\n"
                            "Введите 3 для того, чтобы трансформироваться в ферзя\n"
                            "Введите 4 для того, чтобы трансформироваться в слона\n"))
            chessman = self.GetChessman(x, y)
            if inp == 1:
                transform_to = Rook(chessman.color)
            elif inp == 2:
                transform_to = Knight(chessman.color)
            elif inp == 3:
                transform_to = Queen(chessman.color)
            elif inp == 4:
                transform_to = Bishop(chessman.color)
            else:
                transform_to = Pawn(chessman.color)
            self.board[y][x] = transform_to

        except ValueError:
            print("Введите заново")
            self.Transform(x, y)

    def BackTransformation(self, x, y):
        # Обратная трансформация
        chessman = self.GetChessman(x, y)
        self.board[y][x] = Pawn(chessman.color)

    def IsCheckmate(self):
        # key- king
        # value- position of king
        kings = {}

        for y, i in enumerate(self.board):
            for x, el in enumerate(i):
                if isinstance(el, King):
                    kings.update({el: (x, y)})
        for key, xy in kings.items():
            if self.IsStaleMated(xy):
                if key.color == Color.BLACK:
                    print("Шах черному королю ")
                else:
                    print("Шах белому королю ")

                king_moves = key.GetMoves(self, xy[0], xy[1])
                if len(king_moves) == 0 or any(self.IsStaleMated(i) for i in king_moves):
                    return True, key.color
        return False, None

    def CheckAllKings(self):
        kings = []
        for i in self.board:
            for el in i:
                if isinstance(el, King):
                    kings.update(el)
        if len(kings) == 2:
            return True
        else:
            return False

    def IsStaleMated(self, xy):
        for y, i in enumerate(self.board):
            for x, el in enumerate(i):
                if isinstance(el, ChessMan) and not isinstance(el, King):
                    for move in el.GetMoves(board=self, x=x, y=y):
                        if move == xy:
                            return True
        return False

    def Rollback(self, n):
        # Читаем историю и ходим в обратном порядке
        for i, history_el in enumerate(reversed(self.history)):
            if i == n:
                break
            deleted = history_el.deletedChessman
            if history_el.isTransformed:
                self.BackTransformation(history_el.presentState[0], history_el.presentState[1])
            self.MoveChessman(history_el.presentState, history_el.pastMove)
            if isinstance(deleted, ChessMan):
                self.board[history_el.presentState[1]][history_el.presentState[0]] = deleted
            self.history.remove(history_el)

    @classmethod
    def SetColor(color):
        return '\033[%sm' % color

    def __repr__(self):
        res = "  a   b   c   d   e   f   g  h\n"
        for y in range(8):
            res += "\033[0m" + str(8 - y)
            for x in range(8):
                res += ' ' + str(self.board[y][x]) + ' '
            res += "\n"
        return res
