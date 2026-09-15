from abc import ABC, abstractmethod


##Eine abstrakte Klasse welche Vaterklasse einer jeden Klasse sein soll die Daten aus dem internet für die Karten holt

class KnowledgeSource(ABC):
    def __init__(self, query, topic):
        self.query = query
        self.topic = topic

    @abstractmethod
    def get_information(self) -> tuple[str, str]:
        pass