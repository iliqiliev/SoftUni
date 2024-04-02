class GUIWindow:
    def __init__(self, title: str) -> None:
        self.title = title
        self.minimized = False
        self.saved = False

    @property
    def minimized_state(self) -> str:
        return f"{'un' * (not self.minimized)}minimized"

    @property
    def saved_state(self) -> str:
        return f"{'not ' * (not self.saved)}saved"

    def __str__(self) -> str:
        return (
            f"<{self.title}> state: {self.minimized_state}, {self.saved_state}"
        )
