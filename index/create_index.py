from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import AsyncWebPageReader

def create_index():
    """
    Creates a vector store index from documents and websites.

    :returns: A newly created vector store index.
    :rtype: VectorStoreIndex
    """
    print("Creating index...")
    with open("./data/links.txt", "r", encoding="utf-8") as f:
        content = f.read()

    links = list(filter(lambda l: l != '', map(lambda l: l.strip(), content.split("\n"))))
    documents = AsyncWebPageReader(
        html_to_text=True,
        fail_on_error=True,
    ).load_data(links)

    index = VectorStoreIndex.from_documents(documents)

    print("DONE")

    return index


if __name__ == "__main__":
    create_index()
