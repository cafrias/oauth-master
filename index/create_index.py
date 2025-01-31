from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def create_index():
    """
    Creates a vector store index from documents and websites.

    :returns: A newly created vector store index.
    :rtype: VectorStoreIndex
    """
    print("Creating index...")
    print("\tReading specification", end=" ")
    documents = SimpleDirectoryReader(
        "./data/spec"
    ).load_data()
    print("DONE")

    return VectorStoreIndex.from_documents(documents)


if __name__ == "__main__":
    create_index()
