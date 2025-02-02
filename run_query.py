# noinspection PyUnresolvedReferences
import settings
import index

def main():
    request = input("What do you want to search for?\n")
    print('Retrieving index ...')
    engine = index.get_index().as_query_engine()
    print('Submitting request ...')
    response = engine.query(request)
    print(response)


if __name__ == "__main__":
    main()
