from dotenv import load_dotenv

class KnowledgeExtractor:
    def __init__(self, rawdata):
        self.rawdata = rawdata

    def create_knowledge_item(self):
        text = self.rawdata.content
        request_response = requests.post(
            url= "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer " + load_dotenv("OPENROUTER_API_KEY")
                
            }
        )


