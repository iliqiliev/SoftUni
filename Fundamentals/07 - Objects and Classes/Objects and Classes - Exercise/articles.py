class Article:

    def __init__(self, title: str, content: str, author: str) -> None:
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str) -> None:
        self.content = new_content

    def change_author(self, new_author: str) -> None:
        self.author = new_author

    def rename(self, new_title: str) -> None:
        self.title = new_title

    def __str__(self) -> str:
        return f"{self.title} - {self.content}: {self.author}"
