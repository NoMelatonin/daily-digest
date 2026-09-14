from abc import ABC, abstractmethod

class KnowledgeSource(ABC):
    def __init__(self, topic):
        self.topic = topic

    @abstractmethod
    def get_information(self) -> str:
        pass