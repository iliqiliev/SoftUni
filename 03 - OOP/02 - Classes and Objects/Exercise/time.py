class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours          # Write
        self.minutes = minutes      # Everything
        self.seconds = seconds      # Twice

    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self, tick=1) -> str:
        tick, self.seconds = divmod(self.seconds + tick, Time.max_seconds + 1)
        tick, self.minutes = divmod(self.minutes + tick, Time.max_minutes + 1)
        self.hours = (self.hours + tick) % (Time.max_hours + 1)

        return self.get_time()
