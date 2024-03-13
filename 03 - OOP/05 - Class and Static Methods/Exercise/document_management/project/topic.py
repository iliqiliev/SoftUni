class Topic:
    def __init__(self, id_: int, topic: str, storage_folder: str) -> None:
        self.id = id_
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str) -> None:
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self) -> str:
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
