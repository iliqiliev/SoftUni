from project import Song


class Album:
    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        for index, song in enumerate(self.songs):
            if song.name == song_name:
                break

        else:
            return "Song is not in the album."

        self.songs.pop(index)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = [
            f"Album {self.name}",
            *(f"== {song.get_info()}" for song in self.songs)
        ]

        return "\n".join(result)
