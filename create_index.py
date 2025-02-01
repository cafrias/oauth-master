# noinspection PyUnresolvedReferences
import settings
import index

if __name__ == "__main__":
    newIndex = index.create_index()
    index.save_index(newIndex)
