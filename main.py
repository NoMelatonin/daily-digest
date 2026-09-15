from textknowledgesources.wikipedia import WikipediaSource

def main():
   print("main started")
   first = WikipediaSource( "Isambard Kingdom Brunel")
   result = first.get_information()
   print(result[1])



if __name__ == "__main__":
    main()
