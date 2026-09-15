class KnowledgeItem:
    def __init__(self, subject, question, answer, rawdata, source):
        self.subject = subject
        self.question = question
        self.answer = answer
        self.raw_data = rawdata
        self.source = source


    def show_knowledge_item_content(self):
        print(self.content)

