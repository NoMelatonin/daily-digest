from abc import ABC, abstractmethod

class KnowledgeConverter(ABC):
    def __init__(self, topic, url, content):
        self.topic = topic
        self.url = url
        self.content = content


    def convert_to_knowledge_object(self):
