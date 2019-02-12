from events.event import Event


class NextLevelEvent(Event):
    def __call__(self, *args, **kwargs):
        if len(args) == 0:
            raise ValueError("Must have the next level when raising event")
        if len(args) > 1:
            raise ValueError("Too many arguments")

        super().__call__(*args, **kwargs)
