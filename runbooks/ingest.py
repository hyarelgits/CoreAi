import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("runbooks")

with open("runbooks/cpu_high.txt") as f:
    content = f.read()

collection.add(
    documents=[content],
    ids=["cpu_runbook"]
)

print("Runbook Loaded")

