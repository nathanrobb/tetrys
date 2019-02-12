import pygame

from game.board import Board
from services.level_service import LevelService
from services.lines_cleared_service import LinesClearedService
from services.score_service import ScoreService
from services.speed_service import SpeedService
from game.tetris import Tetris
from services.tetromino_service import TetrominoService
from services.text_service import TextService
from services.theme_service import ThemeService


def main():
    pygame.init()

    board = Board()

    text_service = TextService()
    lines_cleared_service = LinesClearedService(board)
    level_service = LevelService(8, lines_cleared_service, text_service)
    speed_service = SpeedService(level_service)
    tetromino_service = TetrominoService()
    score_service = ScoreService(level_service, text_service, lines_cleared_service)
    theme_service = ThemeService(level_service)

    tetris = Tetris(
        board,
        level_service,
        lines_cleared_service,
        score_service,
        speed_service,
        tetromino_service,
    )

    tetris.run()


if __name__ == '__main__':
    main()
