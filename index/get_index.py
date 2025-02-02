from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.indices.base import BaseIndex

from index.constants import INDEX_STORAGE_DIR, INDEX_ID

def get_index() -> BaseIndex:
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE_DIR)
    return load_index_from_storage(storage_context, index_id=INDEX_ID)
