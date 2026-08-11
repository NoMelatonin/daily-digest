from models import KnowledgeItem
import requests

class WikipediaSource:
    def __init__(self, topic):
        self.topic = topic

    def create_knowledge_item(self):
        url = "https://de.wikipedia.org/w/api.php"
        response = requests.get(url,
                                   params={
                                       "action":"query",
                                       "titles":self.topic,
                                       "prop":"extracts",
                                       "explaintext":True,
                                       "format":"json"
                                   },
                                   headers= {
                                       "User-Agent": "DailyDigest/1.0 (https://github.com/NoMelatonin/daily-digest.git)"
                                   })

        data = response.json()
        information = next(iter(data['query']['pages'].values()))['extract']
        item = KnowledgeItem("Geografie", information, url)
        return item


