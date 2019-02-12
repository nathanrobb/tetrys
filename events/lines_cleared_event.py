from events.event import Event


class LinesClearedEvent(Event):
    def __call__(self, *args, **kwargs):
        if len(args) == 0:
            raise ValueError("Must have the lines cleared when raising event")
        if len(args) > 1:
            raise ValueError("Too many arguments")

        if args[0] < 0:
            raise ValueError('Cannot clear less than zero lines')
        if args[0] > 4:
            raise ValueError('Cannot clear more than four lines')

        super().__call__(*args, **kwargs)
