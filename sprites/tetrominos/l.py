from config import Config
from sprites.block import Block
from sprites.tetromino import Tetromino


class L (Tetromino):
    colour = (0, 0, 255)

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

        self.blocks[0].render(surface, left, top)
        self.blocks[1].render(surface, left + px, top)
        self.blocks[2].render(surface, left + (2 * px), top)
        self.blocks[3].render(surface, left, top + px)

    def add_to_board(self, board, center, bottom):
        top_left = self.blocks[0]
        top_middle = self.blocks[1]
        top_right = self.blocks[2]
        bot_left = self.blocks[3]

        board[bottom - 1][center - 1] = top_left
        board[bottom - 1][center] = top_middle
        board[bottom - 1][center + 1] = top_right
        board[bottom][center - 1] = bot_left

    def rotate_left(self, board):
        return

    def rotate_right(self, board):
        return
