from typing import List

from attr_ex3_document.category import Category
from attr_ex3_document.document import Document
from attr_ex3_document.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        the_category = [c for c in self.categories if c.id == category_id][0]
        the_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        the_topic = [t for t in self.topics if t.id == topic_id][0]
        the_topic.topic = new_topic
        the_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        the_document = [d for d in self.documents if d.id == document_id][0]
        the_document.file_name = new_file_name

    def delete_category(self, category_id):
        the_category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(the_category)

    def delete_topic(self, topic_id):
        the_topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(the_topic)

    def delete_document(self, document_id):
        the_document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(the_document)

    def get_document(self, document_id):
        the_document = [d for d in self.documents if d.id == document_id][0]
        return the_document

    def __repr__(self):
        result = ""
        for d in self.documents:
            result += d.__repr__() + '\n'
        return result










