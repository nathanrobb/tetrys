import pygame


class TextService:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 25)
        self.font_colour = (255, 0, 0)

    def render_text(self, text, surface, left, top):
        surface.blit(self.font.render(text, True, self.font_colour), (left, top))
