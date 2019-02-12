class SpeedService:
    frames_per_drop = [
        48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3
    ]

    def __init__(self, level_service):
        self.level_service = level_service
        self.tick = 0

    def should_drop(self):
        level = self.level_service.level

        if level < 19:
            frames_per_drop = self.frames_per_drop[level]
        elif level < 29:
            frames_per_drop = 2
        else:
            frames_per_drop = 1

        self.tick += 1
        if self.tick >= frames_per_drop:
            self.tick = 0
            return True

        return False
