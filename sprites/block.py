import pygame

from config import Config


class Block:
    def __init__(self, colour, moveable, tetronimo):
        self.colour = colour
        self.is_moveable = moveable
        self.is_tetromino = tetronimo

    def __str__(self):
        return f"{self.is_moveable} {self.is_tetromino}"

    def render(self, surface, left, top):
        if not self.is_tetromino:
            return

        draw_rect = ((left + 1, top + 1), (Config.block_size_px - 2, Config.block_size_px - 2))
        pygame.draw.rect(surface, (255, 255, 255), draw_rect, 0)

        draw_rect = ((left + 2, top + 2), (Config.block_size_px - 4, Config.block_size_px - 4))
        pygame.draw.rect( surface, self.colour, draw_rect, 0)
