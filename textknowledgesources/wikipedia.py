import requests
from .knowledgesource import KnowledgeSource

class WikipediaSource(KnowledgeSource):

    def get_information(self)-> str:
        print("Manische on the beat shabang")
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
        print("received informaiton")
        data = response.json()
        data_to_iterate = data["query"]["pages"]
        content = next(iter(data_to_iterate.values()))["extract"]
        return content







