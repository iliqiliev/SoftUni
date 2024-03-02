from project import Album


class Band:
    def __init__(self, name: str, *albums: Album) -> None:
        self.name = name
        self.albums = [*albums]

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for index, album in enumerate(self.albums):
            if album.name == album_name:
                break

        else:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.pop(index)

        return f"Album {album_name} has been removed."

    def details(self) -> str:
        result = [
            f"Band {self.name}",
            *(album.details() for album in self.albums)
        ]

        return "\n".join(result)
