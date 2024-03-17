from abc import ABC, abstractmethod


class BaseEmail(ABC):
    @property
    @abstractmethod
    def sender(self): ...

    @sender.setter
    @abstractmethod
    def sender(self, sender): ...

    @property
    @abstractmethod
    def receiver(self): ...

    @receiver.setter
    @abstractmethod
    def receiver(self, receiver): ...


class BaseContent(ABC):
    @property
    @abstractmethod
    def content(self): ...

    @content.setter
    @abstractmethod
    def content(self, content): ...


class EmailContent(BaseContent):
    _TAG = "<Iliya Mail>"
    _CLOSING_TAG = _TAG[:1] + "/" + _TAG[1:]

    def __init__(self, content: str) -> None:
        self.content = content

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str) -> None:
        self.__content = "".join((
            self._TAG,
            content,
            self._CLOSING_TAG
        ))

    def __str__(self) -> str:
        return self.content


class Email(BaseEmail):
    def __init__(self, sender: str, receiver: str, content: BaseContent):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    @property
    def sender(self) -> str:
        return self.__sender.title()

    @sender.setter
    def sender(self, sender: str) -> None:
        self.__sender = sender

    @property
    def receiver(self) -> str:
        return self.__receiver.title()

    @receiver.setter
    def receiver(self, receiver: str) -> None:
        self.__receiver = receiver

    def __str__(self) -> str:
        result = (
            f"Sender: {self.sender}",
            f"Receiver: {self.receiver}",
            "Content:",
            f"{self.content}"
        )

        return "\n".join(result)
