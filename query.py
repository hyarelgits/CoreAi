import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("runbooks")

results = collection.query(
    query_texts=["CPU high usage"],
    n_results=2
)

print(results)
