class KnowledgeItem:
    def __init__(self, subject, content, rawdata):
        self.subject = subject
        self.content = content
        self.raw_data = rawdata

    def show_knowledge_item_content(self):
        print(self.content)

class RawData:
    def __init__(self, url, content, subject):
        self.url = url
        self.content = content
        self.subject = subject
