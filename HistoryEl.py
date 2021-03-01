class HistoryEl(object):
    def __init__(self, is_transformed, past_move, present_state, deletedChessman=None):
        self.isTransformed = is_transformed
        self.pastMove = past_move
        self.presentState = present_state
        self.deletedChessman = deletedChessman

