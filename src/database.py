import json
import chromadb

# Create a persistent ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get the sports facts collection
collection = client.get_or_create_collection(name="sports_facts")


def load_facts():
    """Load sports facts from JSON and store them in ChromaDB."""
    with open("data/sports_facts.json", "r", encoding="utf-8") as file:
        facts = json.load(file)

    for index, item in enumerate(facts):
        collection.upsert(
            ids=[str(index)],
            documents=[item["fact"]],
            metadatas=[{"sport": item["sport"]}]
        )

    print("Sports facts successfully loaded into ChromaDB!")


def search_facts(sport, n_results=3):
    """Retrieve relevant facts for the selected sport."""
    results = collection.query(
        query_texts=[sport],
        n_results=n_results
    )

    return results["documents"][0]


if __name__ == "__main__":
    load_facts()