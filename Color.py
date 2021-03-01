class Color(object):
    BLACK = 1
    WHITE = 2
    EMPTY = 0

    @classmethod
    def invert(cls, color):
        if color == cls.EMPTY:
            return color
        return cls.BLACK if color == cls.WHITE else cls.WHITE
