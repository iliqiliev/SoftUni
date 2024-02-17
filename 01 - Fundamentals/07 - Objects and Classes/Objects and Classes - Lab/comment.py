class Comment:

    def __init__(self, username: str, content: str, likes=0) -> None:
        self.username = username
        self.content = content
        self.likes = likes
