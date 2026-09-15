from abc import ABC, abstractmethod

class KnowledgeSource(ABC):
    def __init__(self, query, topic):
        self.query = query
        self.topic = topic

    @abstractmethod
    def get_information(self) -> tuple[str, str]:
        pass