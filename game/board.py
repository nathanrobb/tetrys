import pygame

from sprites.block import Block


class Board:
    block_side_length_px = 20
    blocks_wide = 10
    blocks_high = 20
    max_blocks_high = 25

    width_range = range(blocks_wide - 1, -1, -1)
    left_width_range = range(blocks_wide)
    height_range = range(max_blocks_high - 1, -1, -1)

    def __init__(self):
        self.tetronimo = None
        self.board = [[]]
        self.reset()

    def reset(self):
        self.tetronimo = None
        self.board = [[]]
        for h in range(self.max_blocks_high):
            self.board.append([])
            for w in range(self.blocks_wide):
                self.board[h].append(Block((0, 0, 0), False, False))

    def add_tetronimo(self, t):
        self.tetronimo = t

        # TODO: make these calculated?
        center = 4
        bottom = 4
        t.add_to_board(self.board, center, bottom)

    def update(self, down, left, right):
        if left and right:
            right = False
            left = False

        if self.tetronimo is None:
            return

        can_go_sideways = False
        if left:
            can_go_sideways = self.can_left()
        elif right:
            can_go_sideways = self.can_right()

        if left:
            width_range = self.left_width_range
        else:
            width_range = self.width_range

        for h in self.height_range:
            for w in width_range:
                block = self.board[h][w]
                if block is not None:
                    if block.is_moveable:
                        if can_go_sideways:
                            if left:
                                self.board[h][w] = Block((0, 0, 0), False, False)
                                self.board[h][w - 1] = block
                            elif right:
                                self.board[h][w] = Block((0, 0, 0), False, False)
                                self.board[h][w + 1] = block

        if not down:
            return

        if not self.can_go_down():
            self.tetronimo.set()
            self.tetronimo = None
            return

        for h in self.height_range:
            for w in width_range:
                block = self.board[h][w]
                if block is not None:
                    if block.is_moveable:
                        self.board[h][w] = Block((0, 0, 0), False, False)
                        self.board[h + 1][w] = block

    def can_left(self):
        for h in self.height_range:
            for w in self.left_width_range:
                block = self.board[h][w]
                if block.is_moveable:
                    if w == 0:
                        return False
                    left_block = self.board[h][w - 1]
                    if left_block.is_tetromino and not left_block.is_moveable:
                        return False
        return True

    def can_right(self):
        for h in self.height_range:
            for w in self.width_range:
                block = self.board[h][w]
                if block.is_moveable:
                    if w == self.blocks_wide - 1:
                        return False
                    right_block = self.board[h][w + 1]
                    if right_block.is_tetromino and not right_block.is_moveable:
                        return False
        return True

    def can_go_down(self):
        for h in self.height_range:
            for w in self.width_range:
                block = self.board[h][w]
                if block.is_moveable:
                    if h == self.max_blocks_high - 1:
                        return False

                    bottom_block = self.board[h + 1][w]
                    if bottom_block.is_tetromino and not bottom_block.is_moveable:
                        return False
        return True

    def has_tetromino(self):
        return self.tetronimo is not None

    def render(self, surface):
        bot_px = surface.get_height() - ((surface.get_height() - (self.blocks_high * self.block_side_length_px)) / 2)
        left_px = surface.get_width() - ((surface.get_width() - (self.blocks_wide * self.block_side_length_px)) / 2)
        index_down = self.max_blocks_high - self.blocks_high

        pygame.draw.rect(
            surface,
            (0, 0, 0),
            ((left_px - (10 * self.block_side_length_px), bot_px - (20 * self.block_side_length_px)), (self.block_side_length_px * 10, self.block_side_length_px * 20)),
            0
        )

        curr_h = bot_px
        for h in self.height_range:
            if h < index_down:
                return
            curr_h = curr_h - self.block_side_length_px
            curr_w = left_px
            for w in self.width_range:
                block = self.board[h][w]
                curr_w = curr_w - self.block_side_length_px

                if not block.is_tetromino:
                    continue

                block.render(surface, curr_w, curr_h)

    def is_lost(self):
        for h in self.height_range:
            for w in self.width_range:
                if h <= (self.max_blocks_high - self.blocks_high - 1):
                    block = self.board[h][w]
                    if not block.is_moveable and block.is_tetromino:
                        return True
        return False
