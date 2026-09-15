from textknowledgesources.wikipedia import WikipediaSource
from llmapicalls import generate_question_and_answer_pairs

def main():
    content = """Spring ist ein REST basiertes Java framework, welches es erlaubt methoden von externen servern aufzurufen, indem man http Requests an sie verschickt. Man kann es mit „import org.springframework“ importieren. Dabei gibt es sowohl für den Client als auch für den Server bestimmte anforderungen und allgemeine Strukturelle good practices. 
   Auf der Server seite hat man die sogenannten Controller. Sie sind die Endpunkte der http Requests. Jeden Controller Kennzeichnet man dabei mit einem eigenen Pfad, der es später erlaubt die https Request URL so zu gestalten, dass zwischen den einzelnen controllern unterschieden werden kann. Das kennzeichnet man mit @RequestMapping(value  = “/[name]“). Genau aus dem selben Grund muss man ebenfalss die einzelnen Methoden mit einem URL pfad versehen. Dabei unterscheidet man schon vorher, ob die Methoden eine GET/POST/PUT/DELTE operation ausführen, indem man die methoden mit z.B. @PostMapping(“/[name]“) kennzeichnet. Jede der methoden des controller hat keine normalen formalen Paramter, sondern den Parameter (@RequestBody [Datentyp] [name]). Dadurch nimmt sich  die methode das Objekt direkt aus dem Körper der Request heraus. 
   Eine dritte Möglichkeit ist @RequestParam („name“) Datentyp name. Dann kann man beim formulieren der Request einen Parameter übergeben wie man auf dem Bild unten sieht. Da muss man nur drauf achten dass sowohl der server als auch der client einen wert verlangt und eine Fehlermeldung zurückgibt wenn kein Parameter übergeben wird oder er null ist. Das löst man indem man statt .queryParam, .queryParamIfPresent mit einem Optional als wert gibt, der also statt null ein leeres Optional zurückgibt, sollte es keinen wert geben, wodurch also immer mindestens ein von null verschiedener Wert übergeben wird und es keine NPEs gibt. Das wichtige ist dass das leere Opt.ional auch garnicht übergeben wird, also es so wirkt als gäbe es einfach keine Werte zum übergen Auf der server seite, muss man dann den empfang anpassen. Normalerweise nimmt man ja @RequestParam („name“) Datentyp name. Aber der verlangt dass es valide Parameter gibt. Deshlab nimt man @RequeestParam(value = „name“, required = false) Datentyp name. Dann braucht er keinen Wert."""
   result = generate_question_and_answer_pairs(content)




if __name__ == "__main__":
    main()
