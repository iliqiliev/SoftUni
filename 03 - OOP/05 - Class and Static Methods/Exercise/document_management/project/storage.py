from typing import List, TypeVar
from project import Category, Document, Topic


Item = TypeVar("Item", Category, Document, Topic)


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def _add_item(item: Item, items: List[Item]) -> None:
        if item not in items:
            items.append(item)

    def add_category(self, category: Category) -> None:
        self._add_item(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        self._add_item(topic, self.topics)

    def add_document(self, document: Document) -> None:
        self._add_item(document, self.documents)

    @staticmethod
    def _get_item(item_id: int, items: List[Item]) -> Item:
        try:
            return next(item for item in items if item.id == item_id)

        except StopIteration as error:
            raise LookupError from error

    def edit_category(self, category_id: int, new_name: str) -> None:
        self._get_item(category_id, self.categories).edit(new_name)

    def edit_topic(
        self, topic_id: int, new_topic: str, new_storage_folder: str
    ) -> None:

        self._get_item(topic_id, self.topics).edit(
            new_topic, new_storage_folder
        )

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self._get_item(document_id, self.documents).edit(new_file_name)

    @classmethod
    def _delete_item(cls, item_id: int, items: List[Item]) -> None:
        item = cls._get_item(item_id, items)
        items.remove(item)

    def delete_category(self, category_id: int) -> None:
        self._delete_item(category_id, self.categories)

    def delete_topic(self, topic_id: int) -> None:
        self._delete_item(topic_id, self.topics)

    def delete_document(self, document_id: int) -> None:
        self._delete_item(document_id, self.documents)

    def get_document(self, document_id: int) -> Document:
        return self._get_item(document_id, self.documents)

    def __repr__(self) -> str:
        return "\n".join(str(document) for document in self.documents)
