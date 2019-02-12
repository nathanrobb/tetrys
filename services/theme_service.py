class ThemeService:
    def __init__(self, level_service):
        level_service.next_level_event.append(self.on_next_level)

    def on_next_level(self, level):
        print(f"On_Next_Level {level}")
        # TODO