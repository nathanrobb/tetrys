from events.lines_cleared_event import LinesClearedEvent
from sprites.block import Block


class LinesClearedService:
    def __init__(self, board):
        self.board = board
        self.lines_cleared_event = LinesClearedEvent()

    def check_for_lines(self):
        lines = 0
        h = self.board.max_blocks_high - 1
        board = self.board.board
        while h >= 0:
            completed = True
            for w in self.board.width_range:
                block = board[h][w]
                if not block.is_tetromino or block.is_moveable:
                    completed = False
                    break

            if completed:
                del board[h]
                board.insert(0, [])
                for w in range(self.board.blocks_wide):
                    board[0].append(Block((0, 0, 0), False, False))
                lines += 1
            else:
                h -= 1

        if lines > 0:
            self.lines_cleared_event(lines)
