import requests


# Die Funktion gibt anhand des im Objekt steckenden Themas (z.B. "Isambard Kingdom Brunel") ein Tupel aus der URL und dem Inhalt der Seite aus.
def get_information(topic) -> tuple[str, str, str]:
    url = "https://de.wikipedia.org/w/api.php"
    response = requests.get(
        url,
        params={
            "action": "query",
            "titles": topic,
            "prop": "extracts",
            "explaintext": True,
            "format": "json",
        },
        headers={
            "User-Agent": "DailyDigest/1.0 (https://github.com/NoMelatonin/daily-digest.git)"
        },
    )
    data = response.json()
    data_to_iterate = data["query"]["pages"]
    content = next(iter(data_to_iterate.values()))["extract"]
    return (topic, url, content)







