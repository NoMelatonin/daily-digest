class KnowledgeItem:
    def __init__(self, subject, content, source):
        self.subject = subject
        self.content = content
        self.source = source

    def show_content(self):
        print(self.content)