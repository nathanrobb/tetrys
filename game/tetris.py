import pygame


class Tetris:
    def __init__(self, board, level_service, lines_cleared_service, score_service, speed_service, tetromino_service):
        self.surface = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
        pygame.display.set_caption("Suac Tetris")
        self.board = board
        self.level_service = level_service
        self.lines_cleared_service = lines_cleared_service
        self.score_service = score_service
        self.speed_service = speed_service
        self.tetromino_service = tetromino_service

    def run(self):
        clock = pygame.time.Clock()

        while True:
            left = False
            right = False
            down = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.VIDEORESIZE:
                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    if event.key == pygame.K_LEFT:
                        left = True
                    if event.key == pygame.K_RIGHT:
                        right = True
                    if event.key == pygame.K_DOWN:
                        down = True

            self.surface.fill((255, 255, 255))

            if not self.board.has_tetromino():
                next_t = self.tetromino_service.get_tetromino()
                self.board.add_tetronimo(next_t)

            if self.speed_service.should_drop():
                down = True

            self.board.update(down, left, right)
            self.lines_cleared_service.check_for_lines()

            self.board.render(self.surface)
            self.score_service.render(self.surface, 200, 200)
            self.level_service.render(self.surface, 200, 300, 400)
            self.tetromino_service.render_next(self.surface, 200, 500)

            if self.board.is_lost():
                self.board.reset()
                self.level_service.reset()
                self.score_service.reset()
                self.tetromino_service.reset()

            pygame.display.flip()
            clock.tick(60)
