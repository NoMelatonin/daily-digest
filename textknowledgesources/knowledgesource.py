from abc import ABC, abstractmethod

class KnowledgeSource(ABC):
    def __init__(self, query):
        self.query = query

    @abstractmethod
    def get_information(self) -> tuple[str, str]:
        pass