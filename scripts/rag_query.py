"""
GraphRAG & RAG Engine for Obsidian LLM-Wiki
Requires: `pip install chromadb sentence-transformers networkx`
"""

import os
import re
from pathlib import Path
import networkx as nx
import chromadb
from chromadb.utils import embedding_functions

VAULT_ROOT = Path(r"D:\Obsidian\LLM-Wiki")
CHROMA_DB_DIR = VAULT_ROOT / ".chroma"
WIKI_DIR = VAULT_ROOT / "wiki"

def build_knowledge_graph() -> nx.Graph:
    """Scans the vault to build a topological graph of wikilink relationships."""
    G = nx.Graph()
    wiki_link_pattern = re.compile(r'\[\[(.*?)\]\]')
    
    print(f"🔍 Scanning {WIKI_DIR} for Graph relationships...")
    for filepath in WIKI_DIR.rglob("*.md"):
        try:
            content = filepath.read_text(encoding="utf-8")
            source_node = filepath.stem
            G.add_node(source_node, path=str(filepath))
            
            links = wiki_link_pattern.findall(content)
            for link in links:
                target_node = link.split("|")[0].split("/")[-1]
                G.add_edge(source_node, target_node)
        except Exception as e:
            print(f"Failed to parse {filepath.name}: {e}")
            
    print(f"✅ Built Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")
    return G

def get_graph_neighborhood(graph: nx.Graph, node_name: str, depth=1) -> list:
    """Retrieves the topological neighborhood for a given node."""
    if node_name not in graph:
        return []
    return list(nx.single_source_shortest_path_length(graph, node_name, cutoff=depth).keys())

def init_vector_db():
    """Initializes ChromaDB and embeds the wiki notes."""
    print("⏳ Initializing Vector DB (Chroma)...")
    client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
    
    # We use a default lightweight embedding model from sentence-transformers
    # (Will automatically download the model weights on first run)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    collection = client.get_or_create_collection(
        name="llm_wiki_collection", 
        embedding_function=sentence_transformer_ef
    )
    
    print("📥 Loading wiki documents into the vector database...")
    docs, ids = [], []
    for filepath in WIKI_DIR.rglob("*.md"):
        try:
            # We embed the first 2000 characters as a chunk for speed
            content = filepath.read_text(encoding="utf-8")
            docs.append(content[:2000])
            ids.append(filepath.stem)
        except Exception:
            pass
            
    # Upsert to collection
    if docs:
        collection.upsert(documents=docs, ids=ids)
    
    print(f"✅ Vector DB loaded with {len(ids)} documents.")
    return collection

def semantic_search(collection, query: str) -> str:
    """Queries the vector database for the closest semantic match."""
    print(f"\n🤖 Performing semantic embedding search for: '{query}'")
    results = collection.query(query_texts=[query], n_results=1)
    
    if results['ids'] and results['ids'][0]:
        return results['ids'][0][0]
    return None

def main():
    print("=== Obsidian GraphRAG Engine ===")
    
    G = build_knowledge_graph()
    collection = init_vector_db()
    
    query = input("\nEnter your query: ")
    
    entry_node = semantic_search(collection, query)
    
    if entry_node:
        print(f"\n--- GraphRAG Results ---")
        print(f"Primary Semantic Hit: [[{entry_node}]]")
        
        neighborhood = get_graph_neighborhood(G, entry_node, depth=1)
        if entry_node in neighborhood:
            neighborhood.remove(entry_node)
            
        print(f"Enriched Topological Context (Neighbors): {', '.join(neighborhood)}")
        print("\nNext step: Feed the markdown content of these nodes to the LLM to generate the final answer!")
    else:
        print("No semantic matches found.")

if __name__ == "__main__":
    main()
