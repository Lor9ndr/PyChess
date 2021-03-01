from ChessMan import *
from Empty import Empty
from Rook import Rook


class King(ChessMan):
    IMG = ('♚', '♔')
    moves_made = 0
    can_castling = False
    # key- координаты короля
    # value- координаты ладьи
    castlingCoords = {}

    def GetMoves(self, board, x, y):
        # возможные движения короля

        moves = []
        for j in (y - 1, y, y + 1):
            for i in (x - 1, x, x + 1):
                if i == x and j == y:
                    continue
                if 0 <= i <= 7 and 0 <= j <= 7 and board.GetColor(i, j) != self.color:
                    moves.append((i, j))
        if self.moves_made == 0:
            # Короткая рокировка

            # справа
            try:
                if isinstance(board.board[y][x + 3], Rook) and board.board[y][x + 3].color == self.color \
                        and board.board[y][x + 3].moves_made == 0 \
                        and isinstance(board.board[y][x + 1], Empty) \
                        and isinstance(board.board[y][x + 2], Empty):
                    self.can_castling = True
                    moves.append((x + 2, y))
                    self.castlingCoords.update({(x + 2, y): (x + 3, y)})
                # слева

                if isinstance(board.board[y][x - 3], Rook) and board.board[y][x - 3].color == self.color \
                        and board[y][x + 3].moves_made == 0 \
                        and isinstance(board.board[y][x - 1], Empty)\
                        and isinstance(board.board[y][x - 2], Empty):
                    self.can_castling = True
                    moves.append((x - 2, y))
                    self.castlingCoords.update({(x - 2, y): (x - 3, y)})

                # длинная рокировка

                # справа
                four_el = board.board[y][x + 4]
                first_el = board.board[y][x + 1]
                second_el = board.board[y][x + 2]
                third_el = board.board[y][x + 3]

                if isinstance(four_el, Rook)\
                        and four_el.color == self.color \
                        and four_el.moves_made == 0 \
                        and isinstance(first_el, Empty) \
                        and isinstance(second_el, Empty) \
                        and isinstance(third_el, Empty):
                    self.can_castling = True
                    moves.append((x + 2, y))
                    self.castlingCoords.update({(x + 2, y): (x + 4, y)})

                # слева
                four_el = board.board[y][x - 4]
                first_el = board.board[y][x - 1]
                second_el = board.board[y][x - 2]
                third_el = board.board[y][x - 3]

                if isinstance(four_el, Rook)\
                        and four_el.color == self.color \
                        and four_el.moves_made == 0 \
                        and isinstance(first_el, Empty) \
                        and isinstance(second_el, Empty)\
                        and isinstance(third_el, Empty):
                    self.can_castling = True
                    moves.append((x - 2, y))
                    self.castlingCoords.update({(x - 2, y): (x - 4, y)})
            except IndexError:
                pass

        return moves

    @staticmethod
    def GetRookSide(board, x, y):
        short_right_el = board.board[y][x + 3]
        if isinstance(short_right_el, Rook) \
                and isinstance(board.board[y][x + 2], Empty) \
                and isinstance(board.board[y][x + 1], Empty):
            return 1
        # слева

        short_left_el = board.board[y][x - 3]

        if isinstance(short_left_el, Rook)\
                and isinstance(board.board[y][x - 2], Empty)\
                and isinstance(board.board[y][x - 1], Empty):
            return -1

        # справа
        long_right_el = board.board[y][x + 4]

        if isinstance(long_right_el, Rook) \
                and isinstance(board.board[y][x + 2], Empty) \
                and isinstance(board.board[y][x + 1], Empty) \
                and isinstance(board.board[y][x + 3], Empty):
            return 1

        # слева
        long_left_el = board.board[y][x - 4]

        if isinstance(long_left_el, Rook) \
                and isinstance(board.board[y][x - 3], Empty) \
                and isinstance(board.board[y][x - 2], Empty) \
                and isinstance(board.board[y][x - 1], Empty):
            return -1
