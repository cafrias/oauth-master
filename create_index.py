# noinspection PyUnresolvedReferences
import settings
import index

if __name__ == "__main__":
    new_index = index.create_index()
    index.save_index(new_index)
