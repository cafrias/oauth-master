def run_query(query, index):
    query_engine = index.as_query_engine()
    return query_engine.query(query)
