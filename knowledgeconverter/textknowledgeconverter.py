from models import TextKnowledgeItem

#Die methode sammelt zuerst alle erstellten TextKnowledgeItems in einer Liste und übergibt sie dann als Tupel der liste

def convert_to_knowledge_object(topic: str, url: str, content: tuple[tuple[str, str]]) -> tuple[TextKnowledgeItem]:
    items = []
    for card in content:
        items.append(TextKnowledgeItem(topic, card[0], card[1], url))
    return tuple(items)