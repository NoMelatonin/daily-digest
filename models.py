class TextKnowledgeItem:
    def __init__(self, topic, question, answer, url):
        self.topic = topic
        self.question = question
        self.answer = answer
        self.url = url


    def show_knowledge_item_content(self):
        print(self.content)

