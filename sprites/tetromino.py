class Tetromino:
    blocks = []

    def __init__(self):
        pass

    def render_next(self, surface, left, top):
        pass

    def add_to_board(self, board, center, bottom):
        pass

    def can_rotate_right(self, board):
        pass

    def rotate_right(self, board):
        pass

    def can_rotate_left(self, board):
        pass

    def rotate_left(self, board):
        pass

    def set(self):
        for b in self.blocks:
            b.is_moveable = False
