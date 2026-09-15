class KnowledgeItem:
    def __init__(self, topic, question, answer, rawdata, url):
        self.topic = topic
        self.question = question
        self.answer = answer
        self.raw_data = rawdata
        self.url = url


    def show_knowledge_item_content(self):
        print(self.content)

