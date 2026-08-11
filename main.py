from knowledgesources.wikipedia import WikipediaSource

def main():
    first = WikipediaSource("Mount Everest")
    item = first.create_knowledge_item()
    item.show_content()

if __name__ == "__main__":
    main()
