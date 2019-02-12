class ScoreService:
    colour = (255, 0, 0)
    scores_per_line_combo = [
        0, 40, 100, 300, 1200
    ]

    def __init__(self, level_service, text_service, lines_cleared_service):
        self.level_service = level_service
        self.text_service = text_service

        self.score = 0

        lines_cleared_service.lines_cleared_event.append(self.on_lines_cleared)

    def on_lines_cleared(self, lines_cleared):
        # Refs: https://tetris.fandom.com/wiki/Scoring
        self.score += self.scores_per_line_combo[lines_cleared] * (self.level_service.level + 1)

    def reset(self):
        self.score = 0

    def render(self, surface, left, top):
        self.text_service.render_text(f"Score: {self.score}", surface, left, top)
