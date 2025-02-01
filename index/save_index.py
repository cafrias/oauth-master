from .constants import INDEX_ID, INDEX_STORAGE_DIR

def save_index(index):
    print("Saving index...")
    index.set_index_id(INDEX_ID)
    index.storage_context.persist(INDEX_STORAGE_DIR)
    print("DONE")
    print(f"Saved index to {INDEX_STORAGE_DIR}")
