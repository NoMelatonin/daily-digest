from knowledgesources.wikipedia import WikipediaSource

def main():
   print("main started")
   first = WikipediaSource("Isambard Kingdom Brunel")
   result = first.get_information()
   print(result)



if __name__ == "__main__":
    main()
