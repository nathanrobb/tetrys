from events.next_level_event import NextLevelEvent


class LevelService:
    def __init__(self, start_level, lines_cleared_service, text_service):
        self.start_level = start_level
        self.level = self.start_level
        self.lines = 0
        self.text_service = text_service

        self.next_level_event = NextLevelEvent()

        lines_cleared_service.lines_cleared_event.append(self.on_lines_cleared)

    def on_lines_cleared(self, lines_cleared):
        self.lines += lines_cleared

        # Refs: https://www.reddit.com/r/Tetris/comments/aeork9/us_official_nes_tetris_l29_earlier_transition/ee6ruok/
        # level 4 to 5 = 50, level 9 to 10 = 100, level 18 to 19 = 130
        lines_for_current_level = min((self.level * 10) + 10, max(100, (self.level * 10) - 50))

        if self.lines >= lines_for_current_level:
            self.level += 1
            self.next_level_event(self.level)

    def reset(self):
        self.level = self.start_level
        self.lines = 0
        self.next_level_event(self.level)

    def render(self, surface, left, top_level, top_lines):
        self.text_service.render_text(f"Level: {self.level}", surface, left, top_level)
        self.text_service.render_text(f"Lines: {self.lines}", surface, left, top_lines)
