class Playable:  # can't import Protocol, Judge is ancient
    def play(self) -> str: ...


def start_playing(playable: Playable):
    return playable.play()
