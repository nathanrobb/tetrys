import pygame

from config import Config
from game.seeded_random import SeededRandom
from sprites.tetrominos.i import I
from sprites.tetrominos.j import J
from sprites.tetrominos.l import L
from sprites.tetrominos.o import O
from sprites.tetrominos.s import S
from sprites.tetrominos.t import T
from sprites.tetrominos.z import Z


class TetrominoService:
    def __init__(self):
        self.seeded_random = SeededRandom()
        self.next_tetromino = self.new_tetromino()

        self.font = pygame.font.SysFont('Arial', 25)

    def reset(self):
        self.next_tetromino = self.new_tetromino()

    def render_next(self, surface, left, top):
        surface.blit(self.font.render("Next:", True, (255, 0, 0)), (left, top))
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            ((left, top + 25),
             (Config.block_size_px * 4, Config.block_size_px * 2)),
            0
        )
        self.next_tetromino.render_next(surface, left, top + 25)

    def get_tetromino(self):
        temp = self.next_tetromino
        self.next_tetromino = self.new_tetromino()
        return temp

    def new_tetromino(self):
        random = self.seeded_random.rand_int(6)

        if random == 0:
            return I()
        if random == 1:
            return J()
        if random == 2:
            return L()
        if random == 3:
            return O()
        if random == 4:
            return S()
        if random == 5:
            return T()
        if random == 6:
            return Z()

        raise ValueError()
