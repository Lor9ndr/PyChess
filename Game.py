from ChessBoard import *
from King import King
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
from HistoryEl import HistoryEl


class Game:
    chessDesk = ChessBoard()
    current_color = Color.WHITE

    def __init__(self):
        self.chessDesk.board[1][0] = Pawn(Color.BLACK)
        self.chessDesk.board[1][1] = Pawn(Color.BLACK)
        self.chessDesk.board[1][2] = Pawn(Color.BLACK)
        self.chessDesk.board[1][3] = Pawn(Color.BLACK)
        self.chessDesk.board[1][4] = Pawn(Color.BLACK)
        self.chessDesk.board[1][5] = Pawn(Color.BLACK)
        self.chessDesk.board[1][6] = Pawn(Color.BLACK)
        self.chessDesk.board[1][7] = Pawn(Color.BLACK)
        self.chessDesk.board[0][4] = King(Color.BLACK)
        self.chessDesk.board[0][3] = Queen(Color.BLACK)
        self.chessDesk.board[0][0] = Rook(Color.BLACK)
        self.chessDesk.board[0][7] = Rook(Color.BLACK)
        self.chessDesk.board[0][2] = Bishop(Color.BLACK)
        self.chessDesk.board[0][5] = Bishop(Color.BLACK)
        self.chessDesk.board[0][1] = Knight(Color.BLACK)
        self.chessDesk.board[0][6] = Knight(Color.BLACK)

        self.chessDesk.board[6][0] = Pawn(Color.WHITE)
        self.chessDesk.board[6][1] = Pawn(Color.WHITE)
        self.chessDesk.board[6][2] = Pawn(Color.WHITE)
        self.chessDesk.board[6][3] = Pawn(Color.WHITE)
        self.chessDesk.board[6][4] = Pawn(Color.WHITE)
        self.chessDesk.board[6][5] = Pawn(Color.WHITE)
        self.chessDesk.board[6][6] = Pawn(Color.WHITE)
        self.chessDesk.board[6][7] = Pawn(Color.WHITE)
        self.chessDesk.board[7][4] = King(Color.WHITE)
        self.chessDesk.board[7][3] = Queen(Color.WHITE)
        self.chessDesk.board[7][0] = Rook(Color.WHITE)
        self.chessDesk.board[7][7] = Rook(Color.WHITE)
        self.chessDesk.board[7][2] = Bishop(Color.WHITE)
        self.chessDesk.board[7][5] = Bishop(Color.WHITE)
        self.chessDesk.board[7][1] = Knight(Color.WHITE)
        self.chessDesk.board[7][6] = Knight(Color.WHITE)

    @staticmethod
    def CoordinatesFromString(inp) -> tuple:
        # Конвертация из строки в координаты

        try:
            converter = {
                'a': 0,
                'b': 1,
                'c': 2,
                'd': 3,
                'e': 4,
                'f': 5,
                'g': 6,
                'h': 7
            }
            return converter[inp[0].lower()], 8 - int(inp[1])
        except:
            print("Ошибка")

    @staticmethod
    def FromCoordinatesToString(inp) -> str:
        # Конвертация из координат в строку
        try:
            converter = {
                0: 'a',
                1: 'b',
                2: 'c',
                3: 'd',
                4: 'e',
                5: 'f',
                6: 'g',
                7: 'h'
            }
            res = ''
            if inp:
                for index, el in enumerate(inp):
                    el = el
                    f = converter[el[0]]
                    s = str(8 - el[1])
                    if index == len(inp) - 1:
                        res += f + s
                    else:
                        res += f + s + ','
                return res
            else:
                return "Нет возможных ходов"
        except:
            print("Ошибка")

    def MakeMove(self, from_xy: tuple, to_xy: tuple):
        # процесс трансформации и перехода ячейки
        captured = self.chessDesk.MoveChessman(from_xy, to_xy)
        if self.chessDesk.CanTransform(to_xy[0], to_xy[1]):
            canTrans = True
            self.chessDesk.Transform(to_xy[0], to_xy[1])
        else:
            canTrans = False
        self.AddHistory(captured, from_xy, to_xy, canTrans)
        return self.chessDesk.IsCheckmate()

    def AddHistory(self, captured, from_xy: tuple, to_xy: tuple, canTrans):
        # добавление истории о ходах
        is_transformed = canTrans
        obj = Empty()
        if isinstance(captured, ChessMan):
            obj = captured
        self.chessDesk.history.append(HistoryEl(is_transformed, from_xy, to_xy, deletedChessman=obj))

    def Start(self):
        # UI
        print("Здравствуйте\n"
              "Введите 0 для отката ходов\n"
              "Введите exit для выхода из игры\n"
              "Вводите ячейка в формате буквацифра")
        while True:
            if self.current_color == Color.WHITE:
                print("Ход белых")
            else:
                print("Ход черных")
            print(self.chessDesk)
            inp = input("Выберите ячейку: ")
            if inp == '0':
                inp = int(input("Введите на какое кол-во ходов сделать откат: "))
                self.chessDesk.Rollback(inp)
            elif inp == "exit":
                print("До новых встреч в шахматах")
                break
            else:
                inp = self.CoordinatesFromString(inp)
                selected_chessman: ChessMan = self.chessDesk.GetChessman(inp[0], inp[1])
                if selected_chessman.color == self.current_color:
                    print("Возможные ходы")
                    possible_ways = self.chessDesk.GetMoves(inp[0], inp[1])
                    print(self.FromCoordinatesToString(possible_ways))
                    if len(self.chessDesk.GetMoves(inp[0], inp[1])) == 0:
                        print("Нельзя ходить")
                    else:
                        move = self.CoordinatesFromString(input("Ходите: "))
                        if move in possible_ways:

                            is_check_mate = self.MakeMove(inp, move)
                            self.current_color = Color.invert(self.current_color)
                            if is_check_mate[0]:
                                if is_check_mate[1] == Color.BLACK:
                                    print("Мат черному королю")
                                elif is_check_mate[1] == Color.WHITE:
                                    print("Мат белому королю")
                                if self.SayLastWords():
                                    break

                        else:
                            print("Ошибка")
                else:
                    print("Сейчас ходит другая сторона")

    def SayLastWords(self):
        print(self.chessDesk)
        lastWords = input("Введите 0 чтобы откатить ходы\n"
                          "Введите exit, чтобы выйти\n")
        if lastWords == '0':
            n = int(input("Введите на какое кол-во ходов сделать откат: "))
            self.chessDesk.Rollback(n)
        elif lastWords == 'exit':
            print("До новых встреч")
            return True
        else:
            if self.SayLastWords():
                return True
