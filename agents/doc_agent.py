class DocAgent:
    def __init__(self, vector_store):
        self.store = vector_store

    def query(self, question):
        docs = self.store.search(question)
        return "\n".join(docs)
