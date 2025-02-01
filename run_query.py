# noinspection PyUnresolvedReferences
import settings
import index
import query

if __name__ == "__main__":
    request = input("What do you want to search for?\n")
    indexStore = index.get_index()
    print('Thinking ...')
    response = query.run_query(request, indexStore)
    print(response)
