from config import Config
from sprites.block import Block
from sprites.tetromino import Tetromino


class I (Tetromino):
    colour = (255, 0, 0)

    def __init__(self):
        super().__init__()

        self.blocks = [
            Block(self.colour, True, True),
            Block(self.colour, True, True),
            Block(self.colour, True, True),
            Block(self.colour, True, True),
        ]

    def render_next(self, surface, left, top):
        px = Config.block_size_px

        self.blocks[0].render(surface, left + (0 * px), top)
        self.blocks[1].render(surface, left + (1 * px), top)
        self.blocks[2].render(surface, left + (2 * px), top)
        self.blocks[3].render(surface, left + (3 * px), top)

    def add_to_board(self, board, center, bottom):
        left = self.blocks[0]
        left_middle = self.blocks[1]
        right_middle = self.blocks[2]
        right = self.blocks[3]

        board[bottom][center - 1] = left
        board[bottom][center] = left_middle
        board[bottom][center + 1] = right_middle
        board[bottom][center + 2] = right

    def rotate_left(self, board):
        return

    def rotate_right(self, board):
        return


